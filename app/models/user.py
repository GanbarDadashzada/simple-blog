from app.core.database import Base
from sqlalchemy import String, Integer, Column, DateTime
from datetime import datetime, timezone

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    username = Column(String(255), nullable = True)
    password = Column(String(255), nullable = True)
    email_address = Column(String(255), nullable = True)
    name = Column(String(255), nullable = True)
    surname = Column(String(255), nullable = True)

    date = Column(DateTime, default=datetime.now(timezone.utc))