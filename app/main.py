import uvicorn   #ASGI server that actually runs your FastAPI app. You start your API with it.(Asynchronous Server Gateway Interface)
from fastapi import FastAPI, Query, Header,Form, HTTPException #The main application object. You create app = FastAPI() and attach routes/middleware to it.
from typing import Annotated,List          #Modern way to combine a type with FastAPI’s parameter helpers (e.g., user_id: Annotated[int, Query(ge=1)]).
from app.middleware.cors_middleware import setup_cors
from app.route.ActRouter import ActRouter 
from app.route.CisCaseDetailRouter import CisCaseDetailRouter 

app = FastAPI()
actRouter=ActRouter()
cisCaseDetailRouter=CisCaseDetailRouter()
setup_cors(app)

app.include_router(actRouter.router)
app.include_router(cisCaseDetailRouter.router)

# Add The ROUTE
@app.get("/")
def index():
    return {"Hello": "Fast API, working with Rahul"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)