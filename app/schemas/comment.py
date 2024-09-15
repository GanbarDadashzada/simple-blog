from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class CreateComment(BaseModel):

    blog_id: Optional[int]
    comment_text: Optional[str]
    parent_id: Optional[int]

class EditComment(BaseModel):

    comment_id: Optional[int]
    comment_text: Optional[str]

class DeleteComment(BaseModel):

    comment_id: Optional[int]

class ReadCommentsRequest(BaseModel):

    blog_id: Optional[int]
    skip: Optional[int]
    limit: Optional[int]

class ReadCommentResponse(BaseModel):

    comment_id: Optional[int]
    comment_text: Optional[str]
    user_name: Optional[str]
    user_surname: Optional[str]
    likes_count: Optional[int]
    date_added: Optional[datetime]