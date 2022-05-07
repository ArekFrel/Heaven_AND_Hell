from datetime import datetime

from pesel import Pesel

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Float, Text
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship


from faker import Faker

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    PESEL = Column(String(11), nullable=False, unique=True)
    phone = Column(String(20), nullable=True)
    address = Column(String(100))

    email = relationship('Email', back_populates='student', cascade='all, delete, delete-orphan')
    students_grades = relationship('Grades', back_populates='student')

    def __repr__(self):
        return f'Student({self.id}, {self.first_name}, {self.last_name}, {self.PESEL})'

    @staticmethod
    def create_fake_student():
        fake = Faker()
        return Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            PESEL=str(Pesel.generate())
        )


class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    e_mail = Column(String(50), unique=True)
    user_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    student = relationship('Student', back_populates='email')

    def __repr__(self):
        return f'email ({self.e_mail})'


class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    enrollment_date = Column(DateTime, nullable=False, default=datetime.now)
    PESEL = Column(String(11), nullable=True)
    phone = Column(String(30), nullable=True)
    address = Column(String(100))

    admin_dep = relationship('Departments', back_populates='admins', secondary='administrator')
    courses = relationship('Courses', back_populates='instructors', secondary='course_instructor')

    def __repr__(self):
        return f'Staff ({self.id}, {self.first_name}, {self.last_name}, {self.PESEL})'

    @staticmethod
    def create_fake_teacher():
        fake = Faker()
        return Staff(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone=fake.phone_number(),
            PESEL=str(Pesel.generate()),
        )


class Course(Base):
    __tablename__ = 'courses'

    course_id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    credits = Column(Integer, nullable=False, default=0)
    dep_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    price = Column(Float, nullable=False)

    online = relationship('OnlineCourse', back_populates='course')
    onsite = relationship('OnsiteCourse', back_populates='course')
    department = relationship('Departments', back_populates='courses')
    course_grades = relationship('Grades', back_populates='course')
    instructors = relationship(Staff, back_populates='courses', secondary='course_instructor')


class OnlineCourse(Base):
    __tablename__ = 'online_course'
    course_id = Column(Integer, ForeignKey('course.course_id'), primary_key=True)
    url = Column(String(200), nullable=False)
    course = relationship('Courses', back_populates='online')


class OnsiteCourse(Base):
    __tablename__ = 'onsite_course'
    course_id = Column(Integer, ForeignKey('course.course_id'), primary_key=True)
    address = Column(String(150), nullable=False)
    days = Column(Integer, nullable=False)
    time = Column(DateTime, nullable=False)

    course = relationship('Courses', back_populates='onsite')


class Departments(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    budget = Column(Float, nullable=True)
    address = Column(String(120), nullable=False)

    courses = relationship('Courses', back_populates='department')
    admins = relationship(
        Staff, back_populates='admin_dep', secondary='administrator'
    )

    def __repr__(self):
        return f'Department ({self.id}, {self.name})'


class Grades(Base):
    __tablename__ = 'grades'
    grade_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    student = relationship('Students', back_populates='students_grades')
    course = relationship('Courses', back_populates='course_grades')


class Administrator(Base):
    __tablename__ = 'administrator'
    department_id = Column(Integer, ForeignKey('departments.id'), primary_key=True)
    staff_id = Column(Integer, ForeignKey('staff.id'), primary_key=True)
    enrollment_date = Column(DateTime, nullable=True)


class CourseInstructor(Base):
    __tablename__ = 'course_instructor'
    course_id = Column(Integer, ForeignKey('courses.course_id'), primary_key=True)
    staff_id = Column(Integer, ForeignKey('staff.id'), primary_key=True)
    enrollment_date = Column(DateTime, nullable=True)


def create_fake_teachers(session, count=7):
    for _ in range(count):
        session.add(Staff.create_fake_teacher())
        session.commit()


def create_fake_students(session, count=49):
    for _ in range(count):
        session.add(Student.create_fake_student())
        session.commit()

# class ExamGrades(Base):
#     __tablename__ = "oceny"
