from db.model import Base, create_fake_teachers, create_fake_students
from db.session import Session


if __name__ == "__main__":
    session = Session()
    Base.metadata.create_all(session.get_bind())
    create_fake_teachers(session)
    create_fake_students(session)
