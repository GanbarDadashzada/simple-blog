from app.models.base import Base
from sqlalchemy import String, Integer, Column, DateTime, Text, Boolean, ForeignKey
from datetime import datetime, timezone
from sqlalchemy.orm import relationship

class Comment(Base):

    __tablename__ = "comments"

    id = Column(Integer, primary_key = True)
    comment_text = Column(String(Text), nullable = True)
    blog_id = Column(Integer, ForeignKey("blogs.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    parent_comment = Column(Integer, nullable = True)
    date = Column(DateTime, default=datetime.now(timezone.utc))

    user_relation = relationship("User", back_populates="comment_relation")
    blog_relation = relationship("Blog", back_populates="comment_relation")
    like_relation = relationship("Like", back_populates="comment_relation")