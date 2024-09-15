from typing import Annotated
from fastapi import APIRouter, Depends

from app.core.database import Session, get_session
from app.core.security import Authentication

from app.crud.like import LikeService

from app.schemas.like import AddLikeComment, AddLikeBlog, RemoveLikeFromBlog, RemoveLikeFromComment, GetLikesBlog, GetLikesComment
from app.schemas.registration import Authorization

router = APIRouter()

@router.post("/add_like_blog", tags=["Like"])
async def add_like_blog(username: Annotated[Authorization, Depends(Authentication.active_username)], data: AddLikeBlog, db: Session = Depends(get_session)):
    return await LikeService.add_like_blog(username, data, db)

@router.post("/add_like_comment", tags=["Like"])
async def add_like_comment(username: Annotated[Authorization, Depends(Authentication.active_username)], data: AddLikeComment, db: Session = Depends(get_session)):
    return await LikeService.add_like_comment(username, data, db)

@router.delete("/remove_like_from_blog", tags=["Like"])
async def remove_like_from_blog(username: Annotated[Authorization, Depends(Authentication.active_username)], data: RemoveLikeFromBlog, db: Session = Depends(get_session)):
    return await LikeService.remove_like_from_blog(username, data, db)

@router.post("/remove_like_from_comment", tags=["Like"])
async def remove_like_from_comment(username: Annotated[Authorization, Depends(Authentication.active_username)], data: RemoveLikeFromComment, db: Session = Depends(get_session)):
    return await LikeService.remove_like_from_comment(username, data, db)

@router.post("/get_liked_users_blog", tags=["Like"])
async def get_liked_users_blog(username: Annotated[Authorization, Depends(Authentication.active_username)], data: GetLikesBlog, db: Session = Depends(get_session)):
    return await LikeService.get_liked_users_blog(username, data, db)

@router.post("/get_liked_users_comment", tags=["Like"])
async def get_liked_users_comment(username: Annotated[Authorization, Depends(Authentication.active_username)], data: GetLikesComment, db: Session = Depends(get_session)):
    return await LikeService.get_liked_users_comment(username, data, db)