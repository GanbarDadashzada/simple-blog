from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class CreateBlog(BaseModel):

    content: Optional[str]
    category: Optional[str]
    is_draft: Optional[bool]

class DeleteBlog(BaseModel):

    blog_id: Optional[int]

class EditBlog(BaseModel):

    blog_id: Optional[int]
    content: Optional[str]
    category: Optional[str]
    is_draft: Optional[bool]

class ReadBlogs(BaseModel):

    blog_id: Optional[int]
    content: Optional[str]
    category: Optional[str]
    user_name: Optional[str]
    user_surname: Optional[str]
    comment_count: Optional[int]
    like_count: Optional[int]
    dislike_count: Optional[int]
    date_added: Optional[datetime]
    
class GetBlogRequest(BaseModel):
    
    skip: Optional[int]
    limit: Optional[int]