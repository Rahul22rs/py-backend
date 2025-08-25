from fastapi import APIRouter, HTTPException, Response, status
from app.repo.ActRepo import ActRepo
# from app.request.ActCreateRequest import ActCreateRequest
from app.utils.JwtUtils import JwtUtils
import logging
jwtUtils = JwtUtils()


class ActRouter:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            filename="app.log",
            filemode="a",
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
        self.router = APIRouter(prefix="/act")
        self.repo = ActRepo()
        self.logger = logging.getLogger("ActRouter")
        self.router.add_api_route("/index", self.index, methods=["GET"])
        # self.router.add_api_route("/create", self.create, methods=["POST"])
        self.router.add_api_route("/find/{id}", self.find, methods=["GET"])
        # self.router.add_api_route("/update/{id}", self.update, methods=["PUT"])
        # self.router.add_api_route("/delete/{id}", self.delete, methods=["DELETE"])

    async def index(self):
        try:
            records = self.repo.readAll()
            self.logger.info("------- readAll Called")
            return records
        except Exception:
            self.logger.exception("Act list failed")
            raise HTTPException(status_code=500, detail="Failed to fetch Acts")

    # async def create(self, request: ActCreateRequest, response: Response):
    #     try:
    #         print(request)
    #         self.logger.info(f"------- create : {request.Act_name}")
    #         payload = (
    #             request.model_dump(exclude_unset=True)
    #             if hasattr(request, "model_dump")
    #             else request.dict(exclude_unset=True)
    #         )
    #         result = self.repo.create(payload)
    #         response.status_code = status.HTTP_201_CREATED
    #         return result
    #     except Exception:
    #         self.logger.exception("Act list failed")
    #         raise HTTPException(status_code=500, detail="Failed to fetch Acts")

    async def find(self, id: int):
        record = self.repo.find(id)
        if record is not None:
            return record
        raise HTTPException(422, f" Record not found for id {id}")

    # async def update(self, id: int, request: ActCreateRequest):
    #     record = self.repo.find(id)
    #     if record is not None:
    #         return self.repo.update(
    #             record=record, Act_name=request.Act_name, rating=request.rating
    #         )
    #     raise HTTPException(422, f" Record not found for id {id}")

    # async def delete(self, id: int):
    #     record = self.repo.find(id)
    #     if record is not None:
    #         return self.repo.delete(record=record)
    #     raise HTTPException(422, f" Record not found for id {id}")
