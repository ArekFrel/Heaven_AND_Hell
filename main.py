# from sqlalchemy import create_engine, func, text
from db.session import Session
from db.model import Student, Email
# from sqlalchemy.orm import query
# from mysql.connector import connect, Error


def main():
    session = Session()
    results = session.query(Student.first_name, Student.last_name, Email.e_mail).join(Email).all()
    for result in results:
        print(result)


if __name__ == '__main__':
    main()
