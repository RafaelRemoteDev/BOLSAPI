from sqlalchemy.orm import Session
import database
from database import SessionLocal

class UnitOfWork:
    def __enter__(self):
        self.session = SessionLocal()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()
