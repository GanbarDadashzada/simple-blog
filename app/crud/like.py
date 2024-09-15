from app.core.database import Session

from app.models.like import Like
from app.models.user import User
from app.models.comment import Comment
from app.models.blog import Blog

from app.schemas.registration import Authorization
from app.schemas.like import AddLikeBlog, AddLikeComment, GetLikesBlog, RemoveLikeFromBlog, RemoveLikeFromComment, GetLikesComment, BlogLikesResponse

from app.utils.exception import CustomException

class LikeService:

    async def add_like_blog(username: Authorization, like_data: AddLikeBlog, db: Session):

        user = db.query(User).filter(User.username == username).first()

        like_check = db.query(Like).filter(Like.blog_id == like_data.blog_id).first()
        if like_check:
            raise CustomException(message="User already likes this blog")
        
        like = Like(
            is_dislike = like_data.is_dislike,
            blog_id = like_data.blog_id,
            user_id = user.id
        )
        db.add(like)
        db.commit()

        return {"message": "Like added succesfully"}
    

    async def add_like_comment(username: Authorization, like_data: AddLikeComment, db: Session):

        user = db.query(User).filter(User.username == username).first()

        like_check = db.query(Like).filter(Like.blog_id == like_data.comment_id).first()
        if like_check:
            raise CustomException(message="User already likes this blog")
        
        like = Like(
            is_dislike = False,
            comment_id = like_data.comment_id,
            user_id = user.id
        )
        db.add(like)
        db.commit()

        return {"message": "Like added succesfully"}


    async def remove_like_from_blog(username: Authorization, like_data: RemoveLikeFromBlog, db: Session):

        user = db.query(User).filter(User.username == username).first()

        like = db.query(Like).filter(Like.blog_id == like_data.blog_id,
                                           Like.user_id == user.id).first()
        if not like:
            raise CustomException(message="User does not like this blog")
        
        db.delete(like)
        db.commit()

        return {"message": "Like removed from blog successfully"}


    async def remove_like_from_comment(username: Authorization, like_data: RemoveLikeFromComment, db: Session):

        user = db.query(User).filter(User.username == username).first()

        like = db.query(Like).filter(Like.comment_id == like_data.comment_id,
                                           Like.user_id == user.id).first()
        if not like:
            raise CustomException(message="User does not like this comment")
        
        db.delete(like)
        db.commit()

        return {"message": "Like removed from comment successfully"}
    
    async def get_liked_users_blog(username: Authorization, like_data: GetLikesBlog, db: Session):

        response = []
        
        likes = db.query(Like).filter(Like.blog_id == like_data.blog_id).all()
        if not likes:
            return response
        
        for like in likes:
            user = db.query(User).filter(User.id == like.user_id).first()
            response_data = BlogLikesResponse(
                like_id=like.id,
                user_id=user.id,
                user_name=user.name,
                user_surname=user.surname
            )
            response.append(response_data)
    
        return response

    
    async def get_liked_users_comment(username: Authorization, like_data: GetLikesComment, db: Session):

        response = []
        
        likes = db.query(Like).filter(Like.comment_id == like_data.comment_id).all()
        if not likes:
            return response
        
        for like in likes:
            user = db.query(User).filter(User.id == like.user_id).first()
            response_data = BlogLikesResponse(
                like_id=like.id,
                user_id=user.id,
                user_name=user.name,
                user_surname=user.surname
            )
            response.append(response_data)
    
        return response