from sqlalchemy.orm import Session


class BaseCRUD:

    def __init__(self, db, model):
        self.db: Session = db
        self.model = model

    def create_item(self, item):
        db_item = self.model(title=item.title)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def get_items(self):
        return self.db.query(self.model).all()

    def get_item_by_id(self, id: int):
        return self.db.query(self.model).filter(
            self.model.id == id
        ).first()

    def get_item_by_id_and_title(self, id: int, title: str):
        return self.db.query(self.model).filter(
            self.model.title == title
        ).filter(self.model.id == id).first()

    def get_item_by_title(self, title: str):
        return self.db.query(self.model).filter(
            self.model.title == title
        ).first()

    def update_item_title(self, item, new_title: str):
        db_item = self.db.query(self.model).filter(
            self.model.id == item.id
        ).one_or_none()
        if db_item is None:
            return None
        db_item.title = new_title
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
