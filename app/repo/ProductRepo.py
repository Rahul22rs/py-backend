from app.models.Product import Product
from app.db.config import get_engine, get_session


class ProductRepo:
    def __init__(self) -> None:
        self.engine = get_engine()
        self.session = get_session(self.engine)

    def create(self, product_name: str) -> Product:
        record = Product(product_name=product_name)
        self.session.add_all([record])
        self.session.commit()
        self.session.refresh(record)
        return record

    def update(self, record: Product, name: str, rating: float) -> Product:
        setattr(record, "name", name)
        setattr(record, "rating", rating)
        self.session.commit()
        self.session.refresh(record)
        return record

    def find(self, id: int) -> Product | None:
        return self.session.query(Product).get(id)

    def readAll(self) -> list[Product]:
        return self.session.query(Product).all()

    def delete(self, record: Product) -> None:
        self.session.delete(record)
        self.session.commit()
        return None
