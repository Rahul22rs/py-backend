from app.models.CisCaseDetail import CisCaseDetail
from app.db.config import get_engine, get_session


class CisCaseDetailRepo:
    def __init__(self) -> None:
        self.engine = get_engine()
        self.session = get_session(self.engine)

    # def create(self, data: dict):
    #    record = CisCaseDetail(**data)
    #    self.session.add(record)
    #    self.session.commit()
    #    self.session.refresh(record)
    #    return record

    # def update(self, record: CisCaseDetail, name: str, rating: float) -> CisCaseDetail:
    #     setattr(record, "name", name)
    #     setattr(record, "rating", rating)
    #     self.session.commit()
    #     self.session.refresh(record)
    #     return record

    def find(self, id: int) -> CisCaseDetail | None:
        return self.session.query(CisCaseDetail).get(id)

    def readAll(self) -> list[CisCaseDetail]:
        return self.session.query(CisCaseDetail).all()

    # def delete(self, record: CisCaseDetail) -> None:
    #     self.session.delete(record)
    #     self.session.commit()
    #     return None
