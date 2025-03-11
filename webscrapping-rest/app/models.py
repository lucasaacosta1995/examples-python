from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from app.database import Base
from datetime import datetime

class ScrapingLog(Base):
    __tablename__ = "scraping_request"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(2083), nullable=False)
    scrape_type = Column(String(50), nullable=False)
    success = Column(Boolean, default=False)
    data_size = Column(Integer, default=0)
    save_to_file = Column(Boolean, default=False)  # <-- Agregar este campo
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)
