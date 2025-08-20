from fastapi import FastAPI, Query, Header,Form, HTTPException
from fastapi.staticfiles import StaticFiles
# from req.MultiplyRequest import MultiplyRequest
# from util.AstroTool import AstroTool
from typing import Annotated
# from req.PaginationRequest import PaginationRequest
from app.route.MovieRouter import MovieRouter
# from route.FileUploaderRouter import FileUploaderRouter  
# from route.UserRouter import UserRouter  
# from route.PdfGenRouter import PdfGenRouter
# from route.AdminRouter import AdminRouter
from app.route.ProductRouter import ProductRouter
from app.db.config import get_engine, execute_ddl
# Call the Engine
engine = get_engine()
execute_ddl(engine) 

import os
UPLOAD_DIRECTORY = "uploaded_images"

app = FastAPI()
# app.mount("/uploaded_images", StaticFiles(directory="uploaded_images"), name="uploaded_images")
movieRouter=MovieRouter()
productRouter=ProductRouter()



app.include_router(movieRouter.router)
app.include_router(productRouter.router)
# app.include_router(fileUploaderRouter.router)
# app.include_router(pdfGenRouter.router)
# app.include_router(adminRouter.router)

# Add The ROUTE
@app.get("/")
def index():
    return {"Hello": "Fast API"}


# Raw Body
# @app.post("/multiply")
# def multiply(request: MultiplyRequest):
#     result = request.n1 * request.n2
#     if request.n1 > 1000 or request.n2 > 1000:
#         raise HTTPException(status_code=422, detail="Invalid values")
#     return {"result": result}


# Path Params
# /astro/7
# @app.get("/astro/{luckydigit}")
# async def astro(luckydigit: int):
#     astroTool = AstroTool()
#     return {"forecast": astroTool.getForecast(luckydigit=luckydigit)}


# Query Params
# readAPage?page=2 or readAPage
@app.get("/readAPage")
async def readAPage(page: int = 1):
    return {"response": f"Reading Page number {page}"}


# Form Data
@app.post("/multiply-form")
def multiplyForm(n1: Annotated[int, Form()], n2: Annotated[int, Form()]):
    result = n1 * n2
    return {"result": result}


# Form Data
# @app.get("/search")
# def search(req: Annotated[PaginationRequest, Query()]):

#     return {
#         "page": req.page,
#         "kw": req.kw,
#         "order_by": req.order_by,
#     }


@app.get("/getEmpDetails")
def getEmpDetails(
    id: Annotated[str, Query()],
    lang: Annotated[str | None, Header()] = "en",
):

    return {"id": id, "lang": lang}