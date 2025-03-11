from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
import asyncio
from datetime import datetime
from app.database import SessionLocal
from app.schemas import ScrapeRequest, ScrapeResponse, ScrapeResponseItem
from app.services import scrape_website, log_scraping, save_to_json
from app.config import API_SECRET_KEY, MIN_TIMEOUT, MAX_TIMEOUT

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/scrape/", response_model=ScrapeResponse)
async def scrape_endpoint(
    request: ScrapeRequest, db: Session = Depends(get_db), x_api_token: str = Header(...)
):
    if x_api_token != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Token inválido.")

    if len(request.urls) > 10:
        raise HTTPException(status_code=400, detail="Máximo 10 URLs por solicitud.")

    timeout = max(MIN_TIMEOUT, min(request.timeout, MAX_TIMEOUT))
    
    scrape_tasks = [scrape_website(url, request.scrape_type, timeout) for url in request.urls]
    results = await asyncio.gather(*scrape_tasks)

    response_data = []
    scraped_results = []

    for url, (scraped_data, data_size) in zip(request.urls, results):
        success = bool(scraped_data)
        
        # Se agrega `request.save_to_file` en la llamada
        log_scraping(db, url, request.scrape_type, success, data_size, request.save_to_file)

        response_item = ScrapeResponseItem(
            url=url,
            timestamp=datetime.utcnow(),
            success=success,
            data_size=data_size,
            scraped_data=scraped_data
        )

        response_data.append(response_item)
        if request.save_to_file:
            scraped_results.append({"url": url, "data": scraped_data})

    if request.save_to_file and scraped_results:
        save_to_json(scraped_results)

    return {"results": response_data}

