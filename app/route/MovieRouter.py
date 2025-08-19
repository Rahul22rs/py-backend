from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.repo.MovieRepo import MovieRepo
from app.request.MovieCreateRequest import MovieCreateRequest
from app.request.MovieUpdateRequest import MovieUpdateRequest
import logging


class MovieRouter:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,  # Set the desired logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
            filename="app.log",  # Specify the name of the log file
            filemode="a",  # 'a' for append, 'w' for overwrite
            format="%(asctime)s - %(levelname)s - %(message)s",  # Define the log message format
        )
        self.router = APIRouter(prefix="/movie")
        self.repo = MovieRepo()
        self.logger = logging.getLogger("MovieRouter")
        self.router.add_api_route("/index", self.index, methods=["GET"])
        self.router.add_api_route("/create", self.create, methods=["POST"])
        self.router.add_api_route("/find/{id}", self.find, methods=["GET"])
        self.router.add_api_route("/update/{id}", self.update, methods=["PUT"])
        self.router.add_api_route("/delete/{id}", self.delete, methods=["DELETE"])

    async def index(self):
        records = self.repo.readAll()
        self.logger.info("------- readAll Called")
        return records

    async def create(self, request: MovieCreateRequest):
        self.logger.info(f"------- create : {request.name},{request.rating}")
        records = self.repo.create(request.name, request.rating)
        return records

    async def find(self, id: int):
        record = self.repo.find(id)
        if record is not None:
            return record
        raise HTTPException(422, f" Record not found for id {id}")

    async def update(self, id: int, request: MovieUpdateRequest):
        record = self.repo.find(id)
        if record is not None:
            return self.repo.update(
                record=record, name=request.name, rating=request.rating
            )
        raise HTTPException(422, f" Record not found for id {id}")

    async def delete(self, id: int):
        record = self.repo.find(id)
        if record is not None:
            return self.repo.delete(record=record)
        raise HTTPException(422, f" Record not found for id {id}")
