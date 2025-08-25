from app.models.Act import Act
from app.db.config import get_engine, get_session


class ActRepo:
    def __init__(self) -> None:
        self.engine = get_engine()
        self.session = get_session(self.engine)

    # def create(self, data: dict):
    #    record = Act(**data)
    #    self.session.add(record)
    #    self.session.commit()
    #    self.session.refresh(record)
    #    return record

    # def update(self, record: Act, name: str, rating: float) -> Act:
    #     setattr(record, "name", name)
    #     setattr(record, "rating", rating)
    #     self.session.commit()
    #     self.session.refresh(record)
    #     return record

    def find(self, id: int) -> Act | None:
        return self.session.query(Act).get(id)

    def readAll(self) -> list[Act]:
        return self.session.query(Act).all()

    # def delete(self, record: Act) -> None:
    #     self.session.delete(record)
    #     self.session.commit()
    #     return None
