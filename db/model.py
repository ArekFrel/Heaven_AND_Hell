from datetime import datetime

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Text

from faker import Faker

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    PESEL = Column(String(11), nullable=True)
    phone = Column(String(20), nullable=True)
    address = Column(String(100))

    def __repr__(self):
        return f'Student({self.id}, {self.first_name}, {self.last_name}, {self.PESEL})'

    @staticmethod
    def create_fake_student():
        fake = Faker()
        return Student(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )


def create_fake_students(session, count=0):
    for _ in range(count):
        session.add(Student.create_fake_student())
        session.commit()


class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    enrollment_date = Column(DateTime, nullable=False, default=datetime.now)
    PESEL = Column(String(11), nullable=True)
    phone = Column(String(30), nullable=True)
    address = Column(String(100))

    def __repr__(self):
        return f'Student({self.id}, {self.first_name}, {self.last_name}, {self.PESEL})'

    @staticmethod
    def create_fake_teacher():
        fake = Faker()
        return Staff(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone=fake.phone_number()
        )


def create_fake_teachers(session, count=5):
    for _ in range(count):
        session.add(Staff.create_fake_teacher())
        session.commit()

