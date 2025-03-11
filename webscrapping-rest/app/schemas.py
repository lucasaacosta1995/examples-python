from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ScrapeRequest(BaseModel):
    urls: List[str]
    scrape_type: str
    save_to_file: bool
    timeout: int
    scraped_data: List[str]  # Aseguramos que scraped_data sea una lista de cadenas

    class Config:
        min_anystr_length = 1
        anystr_strip_whitespace = True

class ScrapeResponseItem(BaseModel):
    url: str
    timestamp: datetime
    success: bool
    data_size: int
    scraped_data: Optional[List[str]]

class ScrapeResponse(BaseModel):
    results: List[ScrapeResponseItem]
