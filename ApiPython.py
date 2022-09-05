from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from controllers.StudentController import StudentController

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"Message": "Ha ocurrido un error"})


@app.get("/")
def home():
    return JSONResponse(status_code=200, content={"message": "API Working!!"})


app.include_router(StudentController().router)
