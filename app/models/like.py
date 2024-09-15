from app.core.database import Base
from sqlalchemy import String, Integer, Column, DateTime, Text, Boolean, ForeignKey
from datetime import datetime, timezone
from sqlalchemy.orm import relationship

class Like(Base):

    __tablename__ = "likes"

    id = Column(Integer, primary_key = True)
    is_dislike = Column(Boolean, nullable=True)
    blog_id = Column(Integer, ForeignKey("blogs.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    comment_id = Column(Integer, ForeignKey("comments.id"))
    date = Column(DateTime, default=datetime.now(timezone.utc))

    user_relation = relationship("User", back_populates="users.id")
    blog_relation = relationship("Blog", back_populates="blogs.id")
    comment_relation = relationship("Comment", back_populates="comments.id")