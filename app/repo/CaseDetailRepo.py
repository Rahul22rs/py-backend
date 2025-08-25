from app.models.CaseDetail import CaseDetail
from app.db.config import get_engine, get_session


class CaseDetailRepo:
    def __init__(self) -> None:
        self.engine = get_engine()
        self.session = get_session(self.engine)

    # def create(self, data: dict):
    #    record = CaseDetail(**data)
    #    self.session.add(record)
    #    self.session.commit()
    #    self.session.refresh(record)
    #    return record

    # def update(self, record: CaseDetail, name: str, rating: float) -> CaseDetail:
    #     setattr(record, "name", name)
    #     setattr(record, "rating", rating)
    #     self.session.commit()
    #     self.session.refresh(record)
    #     return record

    def find(self, id: int) -> CaseDetail | None:
        return self.session.query(CaseDetail).get(id)

    def readAll(self) -> list[CaseDetail]:
        return self.session.query(CaseDetail).all()

    # def delete(self, record: CaseDetail) -> None:
    #     self.session.delete(record)
    #     self.session.commit()
    #     return None
