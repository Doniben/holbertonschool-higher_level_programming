#!/usr/bin/python3
""" Module 7-model_state_fetch_all """
from sys import argv
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import (create_engine, MetaData, Table, select)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in session.query(State, City).filter(
                City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(i.State.name, i.City.id, i.City.name))
    session.close()
