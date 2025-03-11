# scraper.py
import aiohttp
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime
from app.models import ScrapeResponseItem
from app.database import SessionLocal
from app.config import MIN_TIMEOUT, MAX_TIMEOUT

async def fetch_html(session, url, timeout):
    """Descarga la página con timeout."""
    try:
        async with session.get(url, timeout=timeout) as response:
            return await response.text()
    except Exception:
        return None

async def scrape_website(url: str, scrape_type: str, timeout: int):
    """Scrapea una URL y retorna los datos."""
    async with aiohttp.ClientSession() as session:
        html = await fetch_html(session, url, timeout)
        if not html:
            return None, 0
        
        soup = BeautifulSoup(html, "html.parser")
        if scrape_type == "text":
            # Aseguramos que los datos devueltos sean una lista
            data = [soup.get_text(separator=" ", strip=True)]  # Es una lista con un solo elemento
        elif scrape_type == "images":
            data = [img["src"] for img in soup.find_all("img") if "src" in img.attrs]
        elif scrape_type == "links":
            data = [a["href"] for a in soup.find_all("a") if "href" in a.attrs]
        else:
            return None, 0

        return data, len(str(data))  # Devuelve los datos scrapeados como lista y su tamaño

def log_scraping(db, url: str, scrape_type: str, success: bool, data_size: int, save_to_file: bool):
    """Guarda el resultado en la base de datos, incluyendo save_to_file."""
    log = ScrapingLog(
        url=url,
        scrape_type=scrape_type,
        success=success,
        data_size=data_size,
        save_to_file=save_to_file
    )
    db.add(log)
    db.commit()

def save_to_json(results):
    """Guarda los datos scrapeados en un archivo JSON dentro de la carpeta 'files_jsons'."""
    timestamp = datetime.utcnow().isoformat().replace(":", "-").replace("T", "_")  # Reemplaza caracteres inválidos
    folder_path = "files_jsons"
    os.makedirs(folder_path, exist_ok=True)  # Crea la carpeta si no existe

    filename = os.path.join(folder_path, f"scraped_{timestamp}.json")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
    
    return filename
