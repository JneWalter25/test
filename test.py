from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
import datetime

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    date = Column(Date, default=datetime.datetime.today())
    deadline = Column(Date, default=datetime.datetime.today)


class Database1:
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


class date1:

    def elegirmes(mes):
        if mes == "01":
            Menu.mes2 = "Jan"
        elif mes == "02":
            Menu.mes2 = "Feb"
        elif mes == "03":
            Menu.mes2 = "Mar"
        elif mes == "04":
            Menu.mes2 = "Apr"
        elif mes == "05":
            Menu.mes2 = "May"
        elif mes == "06":
            Menu.mes2 = "Jun"
        elif mes == "07":
            Menu.mes2 = "Jul"
        elif mes == "08":
            Menu.mes2 = "Aug"
        elif mes == "09":
            Menu.mes2 = "Sep"
        elif mes == "10":
            Menu.mes2 = "Oct"
        elif mes == "11":
            Menu.mes2 = "Nov"
        elif mes == "12":
            Menu.mes2 = "Dec"

class Menu(Database1, Table, date1):
    while True:
        print("1) Today's tasks")
        print("2) Week's tasks")
        print("3) All tasks")
        print("4) Add task")
        print("0) Exit")
        elec = int(input())
        if elec == 1:
            d = datetime.datetime.now()
            print(d)
            print(d.strftime("%m"))
            d = datetime.datetime.now()
            print(d)
            mes = d.strftime("%m")
            mes2 = ""
            rows = Database1.session.query(Table).all()
            mes2 = date1.elegirmes(mes)
            print(mes2)
            print("Today:")
            j = 0
            for row in rows:
                row2 = rows[j]
                print(row2.task)
                j += 1
            if j == 0:
                print("Nothing to do!")

        elif elec == 2:
            taskin = input()
            new_row = Table(task=taskin,
                            deadline=datetime.today().date())
            Database1.session.add(new_row)
            Database1.session.commit()
            rows = Database1.session.query(Table).all()
            first_row = rows[0]  # In case rows list is not empty
            print("The task has been added!")
        elif elec == 0:
            break



Table
Database1
Menu
date1.elegirmes