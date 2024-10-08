from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.api.endoints import login, blog, comment, like
from app.utils.exception import custom_exception, CustomException
app=FastAPI()

routers = [login.router, blog.router, like.router, comment.router]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )

for route in routers:
    app.include_router(route)

app.add_exception_handler(CustomException, custom_exception)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
