from app.models.base import Base
from sqlalchemy import String, Integer, Column, DateTime, Text, Boolean, ForeignKey
from datetime import datetime, timezone
from sqlalchemy.orm import relationship

class Blog(Base):

    __tablename__ = "blogs"

    id = Column(Integer, primary_key = True)
    content = Column(String(Text), nullable = True)
    category = Column(String(255), nullable = True)
    is_draft = Column(Boolean, nullable = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime, default=datetime.now(timezone.utc))

    user_relation = relationship("User", back_populates="blog_relation")
    comment_relation = relationship("Comment", back_populates="blog_relation")
    like_relation = relationship("Like", back_populates="blog_relation")