from app.models.base import Base
from sqlalchemy import String, Integer, Column, DateTime
from datetime import datetime, timezone
from sqlalchemy.orm import relationship

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    username = Column(String(255), unique = True)
    password = Column(String(255), nullable = True)
    email_address = Column(String(255), nullable = True)
    name = Column(String(255), nullable = True)
    surname = Column(String(255), nullable = True)
    date = Column(DateTime, default=datetime.now(timezone.utc))

    blog_relation = relationship("Blog", back_populates="user_relation")
    comment_relation = relationship("Comment", back_populates="user_relation")
    like_relation = relationship("Like", back_populates="user_relation")