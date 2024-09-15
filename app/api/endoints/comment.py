from typing import Annotated
from fastapi import APIRouter, Depends

from app.core.database import Session, get_session
from app.core.security import Authentication

from app.crud.comment import CommentService

from app.schemas.comment import CreateComment, EditComment, DeleteComment, ReadCommentsRequest
from app.schemas.registration import Authorization

router = APIRouter()

@router.post("/create_comment", tags=["Comment"])
async def create_comment(username: Annotated[Authorization, Depends(Authentication.active_username)], data: CreateComment, db: Session = Depends(get_session)):
    return await CommentService.create_comment(username, data, db)

@router.put("/edit_comment", tags=["Comment"])
async def edit_comment(username: Annotated[Authorization, Depends(Authentication.active_username)], data: EditComment, db: Session = Depends(get_session)):
    return await CommentService.edit_comment(username, data, db)

@router.delete("/delete_comment", tags=["Comment"])
async def delete_comment(username: Annotated[Authorization, Depends(Authentication.active_username)], data: DeleteComment, db: Session = Depends(get_session)):
    return await CommentService.delete_comment(username, data, db)

@router.post("/read_comments_of_blog", tags=["Comment"])
async def read_comments_of_blog(username: Annotated[Authorization, Depends(Authentication.active_username)], data: ReadCommentsRequest, db: Session = Depends(get_session)):
    return await CommentService.read_comments_of_blog(username, data, db)