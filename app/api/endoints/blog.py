from typing import Annotated
from fastapi import APIRouter, Depends, Query

from app.core.database import Session, get_session
from app.core.security import Authentication

from app.crud.blog import BlogService

from app.schemas.blog import CreateBlog, EditBlog, DeleteBlog
from app.schemas.registration import Authorization

router = APIRouter()

@router.post("/create_blog", tags=["Blog"])
async def create_blog(username: Annotated[Authorization, Depends(Authentication.active_username)], data: CreateBlog, db: Session = Depends(get_session)):
    return await BlogService.create_blog(username, data, db)

@router.delete("/delete_blog", tags=["Blog"])
async def delete_blog(username: Annotated[Authorization, Depends(Authentication.active_username)], data: DeleteBlog, db: Session = Depends(get_session)):
    return await BlogService.delete_blog(username, data, db)

@router.put("/edit_blog", tags=["Blog"])
async def edit_blog(username: Annotated[Authorization, Depends(Authentication.active_username)], data: EditBlog, db: Session = Depends(get_session)):
    return await BlogService.edit_blog(username, data, db)

@router.get("/get_blogs", tags=["Blog"])
async def get_blogs(username: Annotated[Authorization, Depends(Authentication.active_username)], skip: int = Query(1, ge=1), limit: int = Query(10, gt=0), db: Session = Depends(get_session)):
    return await BlogService.get_blogs(username, skip, limit, db)