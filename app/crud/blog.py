from fastapi import HTTPException

from app.core.database import Session

from app.utils.exception import CustomException

from app.models.user import User
from app.models.blog import Blog

from app.schemas.registration import Authorization
from app.schemas.blog import CreateBlog, DeleteBlog, EditBlog, GetBlogRequest, ReadBlogs


class BlogService:


    async def create_blog(username: Authorization, blog_data: CreateBlog, db: Session):
        """
        Create a new blog post or a draft.

        :username: The username of the authenticated user.
        :blog_data: An instance of CreateBlog containing the blog content, category, and draft status.
        :db: The database session for interacting with the database.
        :return: A dictionary with a success message indicating whether the blog was created as a draft or published.
        """
        user = db.query(User).filter(User.username == username).first()
        
        blog = Blog(
            content = blog_data.content,
            category = blog_data.category,
            is_draft = blog_data.is_draft,
            user_id = user.id
        )
        db.add(blog)
        db.commit()

        response_message = "Draft created successfully" if blog_data.is_draft is True else "Blog created sucessfully"

        return {"message": response_message}
    

    async def delete_blog(username: Authorization, blog_data: DeleteBlog, db: Session):
        """
        Delete an existing blog post.

        :username: The username of the authenticated user.
        :blog_data: An instance of DeleteBlog containing the blog ID to be deleted.
        :db: The database session for interacting with the database.
        :raises CustomException: If the blog post is not found or does not belong to the user.
        :return: A dictionary with a success message indicating the blog was deleted.
        """
        user = db.query(User).filter(User.username == username).first()

        blog = db.query(Blog).filter(Blog.id == blog_data.blog_id, Blog.user_id == user.id).first()
        if not blog:
            raise CustomException(message="Blog not found")
        
        db.delete(blog)
        db.commit()

        return {"message": "Blog deleted successfully"}
    
    
    async def edit_blog(username: Authorization, blog_data: EditBlog, db: Session):
        """
        Edit an existing blog post.

        :username: The username of the authenticated user.
        :blog_data: An instance of EditBlog containing the blog ID and the fields to be updated.
        :db: The database session for interacting with the database.
        :raises CustomException: If the blog post is not found or does not belong to the user.
        :return: A dictionary with a success message indicating the blog was updated.
        """
        user = db.query(User).filter(User.username == username).first()

        blog = db.query(Blog).filter(Blog.id == blog_data.blog_id, Blog.user_id == user.id).first()
        if not blog:
            raise CustomException("Blog not found")
        
        for key, value in blog_data.model_dump().items():
            if key != "blog_id" or value != None:
                setattr(blog, key, value)
        
        db.commit()

        return {"message": "Blog updated successfully"}
    

    async def get_blogs(username: Authorization, data: GetBlogRequest, db: Session):
        """
        Retrieve a list of blog posts with pagination.
        :param skip: The number of items to skip.
        :param limit: The maximum number of items to return.
        :return: A list of blog posts.
        """
        blogs = db.query(Blog).filter(Blog.is_draft == False).offset(data.skip).limit(data.limit).all()

        response = []

        if not blogs:
            return response

        for blog in blogs:
            
            like_counter = sum(1 for relation in blog.like_relation if not relation.is_dislike)
            dislike_counter = sum(1 for relation in blog.like_relation if relation.is_dislike)
            
            blog_by = db.query(User).filter(User.id == blog.user_id).first()
            response_data = ReadBlogs(
                blog_id=blog.id,
                content=blog.content,
                category=blog.category,
                user_name=blog_by.name,
                user_surname=blog_by.surname,
                comment_count=len(blog.comment_relation),
                like_count=like_counter,
                dislike_count=dislike_counter,
                date_added=blog.date
            )
            response.append(response_data)

        return response

