from datetime import datetime

from faker import Faker
from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey, Float
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# just to check if it works


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    reg_date = Column(DateTime, nullable=False, default=datetime.now)

    articles = relationship(
        "Article", back_populates="author",
        # cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return f"User({self.id}, {self.first_name}, {self.last_name}, {self.email})"

    @staticmethod
    def create_fake_user():
        fake = Faker()
        return User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email()
        )