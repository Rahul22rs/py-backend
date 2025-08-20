from fastapi import APIRouter, HTTPException, Depends
# from sqlalchemy.orm import Session
from app.repo.ProductRepo import ProductRepo
from app.request.ProductCreateRequest import ProductCreateRequest
# from app.request.MovieUpdateRequest import MovieUpdateRequest
import logging


class ProductRouter:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,  # Set the desired logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
            filename="app.log",  # Specify the name of the log file
            filemode="a",  # 'a' for append, 'w' for overwrite
            format="%(asctime)s - %(levelname)s - %(message)s",  # Define the log message format
        )
        self.router = APIRouter(prefix="/product")
        self.repo = ProductRepo()
        self.logger = logging.getLogger("PrioductRouter")
        self.router.add_api_route("/index", self.index, methods=["GET"])
        self.router.add_api_route("/create", self.create, methods=["POST"])
        self.router.add_api_route("/find/{id}", self.find, methods=["GET"])
        self.router.add_api_route("/update/{id}", self.update, methods=["PUT"])
        self.router.add_api_route("/delete/{id}", self.delete, methods=["DELETE"])

    async def index(self):
        records = self.repo.readAll()
        self.logger.info("------- readAll Called")
        return records

    async def create(self, request: ProductCreateRequest):
        self.logger.info(f"------- create : {request.product_name}")
        records = self.repo.create(request.product_name)
        return records

    async def find(self, id: int):
        record = self.repo.find(id)
        if record is not None:
            return record
        raise HTTPException(422, f" Record not found for id {id}")

    async def update(self, id: int, request: ProductCreateRequest):
        record = self.repo.find(id)
        if record is not None:
            return self.repo.update(
                record=record, product_name=request.product_name, rating=request.rating
            )
        raise HTTPException(422, f" Record not found for id {id}")

    async def delete(self, id: int):
        record = self.repo.find(id)
        if record is not None:
            return self.repo.delete(record=record)
        raise HTTPException(422, f" Record not found for id {id}")
