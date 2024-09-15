from app.core.database import Session

from app.models.comment import Comment
from app.models.user import User

from app.schemas.comment import CreateComment, EditComment, DeleteComment, ReadCommentResponse, ReadCommentsRequest
from app.schemas.registration import Authorization

from app.utils.exception import CustomException

class CommentService:


    async def create_comment(username: Authorization, comment_data: CreateComment, db: Session):

        user = db.query(User).filter(User.username == username).first()

        comment = Comment(
            comment_text = comment_data.comment_text,
            parent_comment = None if comment_data.parent_id is None else comment_data.parent_id,
            blog_id = comment_data.blog_id,
            user_id = user.id
        )
        db.add(comment)
        db.commit()

        return {"message": "Comment created successfully"}
        
    
    async def edit_comment(username: Authorization, comment_data: EditComment, db: Session):

        user = db.query(User).filter(User.username == username).first()
        comment = db.query(Comment).filter(Comment.id == comment_data.comment_id, Comment.user_id == user.id).first()
        
        if not comment:
            raise CustomException(message="Comment not found")
        
        comment.comment_text = comment_data.comment_text

        db.commit()

        return {"message": "Comment edited successfully"}
    

    async def delete_comment(username: Authorization, comment_data: DeleteComment, db: Session):

        user = db.query(User).filter(User.username == username).first()
        comment = db.query(Comment).filter(Comment.id == comment_data.comment_id, Comment.user_id == user.id).first()

        if not comment:
            raise CustomException(message="Comment not found")
        
        db.delete(comment)
        db.commit()

        return {"message": "Comment deleted successfully"}


    async def read_comments_of_blog(username: Authorization, comment_data: ReadCommentsRequest, db: Session):

        comments = db.query(Comment).filter(Comment.id == comment_data.comment_id,
                                            Comment.blog_id == comment_data.blog_id).offset(comment_data.skip).limit(comment_data.limit).all()

        response = []

        if not comments:
            return response
        
        for comment in comments:
            user = db.query(User).filter(User.id == comment.user_id).first()
            
            response_data = ReadCommentResponse(
                comment_id=comment.id,
                comment_text=comment.comment_text,
                user_name=user.name,
                user_surname=user.surnamem,
                likes_count=len(comment.like_relation),
                date_added=comment.date
            )
            response.append(response_data)

        return response