#!/usr/bin/env python3

from datetime import datetime

from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.grade}"

if __name__ == '__main__':

    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    ###CREATE SESSION###
    Session = sessionmaker(bind=engine)
    session = Session()

    ###STUDENT OBJECTS###
    albert_einstein = Student(
        name="Albert Einstein",
        email="albert.einstein@zurich.edu",
        grade=6,
        birthday=datetime(
            year=1879,
            month=3,
            day=14
        ),
    )


    # (session.add(albert_einstein)
    # session.commit()
    # print(f"New student ID is {albert_einstein.id}."))


    alan_turing = Student(
        name="Alan Turing",
        email="alan.turing@sherborne.edu",
        grade=11,
        birthday=datetime(
            year=1912,
            month=6,
            day=23
        ),
    )

    ###TO ADD MULTIPLE STUDENTS AT ONCE:###
    session.bulk_save_objects([albert_einstein, alan_turing])
    session.commit()

    # print(f"New student ID is {albert_einstein.id}.")
    # print(f"New student ID is {alan_turing.id}.")

    # students = session.query(Student)
    # print([student for student in students])


    ####TO PRINT ALL NAMES###
    # names = session.query(Student.name).all()
    # print(names)

    ###PRINT NAMES BY ALPHABETICAL ORDER###
    # students_by_name = session.query(
    #     Student.name).order_by(
    #     Student.name).all()
    # print(students_by_name)

    ###PRINT NAME BY GRADE (DESCENDING)###
    # students_by_grade_desc = session.query(
    #         Student.name, Student.grade).order_by(
    #         desc(Student.grade)).all()
    # print(students_by_grade_desc)


    #TO FIND OLDEST STUDENT BY GRADE (NOT BY BIRTHDAY!!)
    # oldest_student = session.query(
    #         Student.name, Student.birthday).order_by(
    #         desc(Student.grade)).limit(1).all()
    # print(oldest_student)

    #TO FIND OLDEST STUDENT BY GRADE (NOT BY BIRTHDAY!!) USING .first()
    # oldest_student = session.query(
    #         Student.name, Student.birthday).order_by(
    #         desc(Student.grade)).first()
    # print(oldest_student)

    ###COUNT STUDENTS###
    student_count = session.query(func.count(Student.id)).first()
    print(student_count)
