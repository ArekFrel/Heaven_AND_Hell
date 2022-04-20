from sqlalchemy import create_engine
from db.session import Session
from db.model import Student
from sqlalchemy import text


def main():
    # engine = create_engine('sqlite:///database/heaven_and_hell.sqlite')
    # imiona = engine.execute('Select name from names LIMIT 2')
    #
    # for imie in imiona:
    #     print(imie)

    session = Session()
    result = session.query(Student).filter(text("id=:id")).params(id=5)
    for student in result:
        print(student)

    print("-----------------")

    sql_statement = text("SELECT * FROM students WHERE id <:max")
    result = session.query(Student).from_statement(sql_statement).params(max=5)
    for student in result:
        print(student)


if __name__ == '__main__':
    main()
