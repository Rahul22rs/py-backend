from app.models.Movie import Movie
from app.db.config import get_engine, get_session


class MovieRepo:
    def __init__(self) -> None:
        self.engine = get_engine()
        self.session = get_session(self.engine)

    def create(self, name: str, rating: float) -> Movie:
        record = Movie(name=name, rating=rating)
        self.session.add_all([record])
        self.session.commit()
        self.session.refresh(record)
        return record

    def update(self, record: Movie, name: str, rating: float) -> Movie:
        setattr(record, "name", name)
        setattr(record, "rating", rating)
        self.session.commit()
        self.session.refresh(record)
        return record

    def find(self, id: int) -> Movie | None:
        return self.session.query(Movie).get(id)

    def readAll(self) -> list[Movie]:
        return self.session.query(Movie).all()

    def delete(self, record: Movie) -> None:
        self.session.delete(record)
        self.session.commit()
        return None
