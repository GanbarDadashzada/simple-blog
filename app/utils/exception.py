from fastapi.responses import JSONResponse

class CustomException(Exception):

    def __init__(self, message: str):
        self.detail = message

async def custom_exception(exc: CustomException):
    return JSONResponse(content={"message": f"{exc.detail}"}, status_code=400)

