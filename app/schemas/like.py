from pydantic import BaseModel
from typing import Optional


class AddLikeBlog(BaseModel):

    is_dislike: Optional[bool]
    blog_id: Optional[int]


class AddLikeComment(BaseModel):

    comment_id: Optional[int]


class RemoveLikeFromBlog(BaseModel):

    blog_id: Optional[int]


class RemoveLikeFromComment(BaseModel):

    comment_id: Optional[int]


class GetLikesBlog(BaseModel):

    blog_id: Optional[int]


class GetLikesComment(BaseModel):

    comment_id: Optional[int]


class BlogLikesResponse(BaseModel):

    like_id: Optional[int]
    user_id: Optional[int]
    user_name: Optional[str]
    user_surname: Optional[str]