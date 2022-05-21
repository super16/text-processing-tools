from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta

from typing import Any


class BaseCRUDL:
    """
    Basic CRUDL class to operate with models.
    """

    def __init__(
        self, db: Session,
        model: DeclarativeMeta
    ) -> None:
        """
        BaseCRUDL class constructor.

        Args:
          db (Session): SQLAlchemy Session class
          (interface to DB).
          model (DeclarativeMeta): model class.
        """
        self.db: Session = db
        self.model: DeclarativeMeta = model

    def create_item(self, item):
        """
        Create model item.

        Args:
          item: Pydantic model (schema) to create data.

        Returns:
          Created model item.
        """
        db_item = self.model(title=item.title)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def delete_item(self, id: int):
        """
        Delete model item.

        Args:
          id: Id value of object to delete.

        Returns:
          Deleted model item.
        """
        db_item = self.read_item_by_attr('id', id)
        if db_item is None:
            return None
        self.db.delete(db_item)
        self.db.commit()
        return db_item

    def read_items(self):
        """
        Read all model items from DB.

        Returns:
          List of all model items.
        """
        return self.db.query(self.model).order_by('id').all()

    def read_item_by_attr(self, attr: str, value: Any):
        """
        Read model item from DB by attribute and
        its value, if any.

        Args:
          attr (str): Attribute name.
          value: value to find by.

        Returns:
          Found model item, if any.
        """
        return self.db.query(self.model).filter(
            getattr(self.model, attr) == value
        ).first()

    def get_item_by_id_and_title(self, id: int, title: str):
        """
        Temporary method.
        """
        return self.db.query(self.model).filter(
            self.model.title == title
        ).filter(self.model.id == id).first()

    def update_item_by_attr(self, item, attr: str, value: Any):
        """
        Update model item from DB by attribute and
        its value, if any.

        Args:
          attr (str): Attribute name.
          value: value to find.

        Returns:
          Updated model item, if was found any to update.
        """
        db_item = self.db.query(self.model).filter(
            self.model.id == item.id
        ).one_or_none()
        if db_item is None:
            return None
        setattr(db_item, attr, value)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item
