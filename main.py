from sqlalchemy import create_engine
from db.session import Session
from db.model import Student


def main():
    # engine = create_engine('sqlite:///database/heaven_and_hell.sqlite')
    # imiona = engine.execute('Select name from names LIMIT 2')
    #
    # for imie in imiona:
    #     print(imie)

    session = Session()
    result = session.query(Student.first_name)
    for name in result:
        print(name[0])





if __name__ == '__main__':
    main()
