#!/usr/bin/python3
"""
Python file similar to model_state.py named
model_city.py that contains the class definition of a City
"""

import sys
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


def fetch_all():
    """
    Your script should take 3 arguments: mysql username,
    mysql password and database name.
    You must use the module SQLAlchemy
    You must import State and Base from model_state - from
    model_state import Base, State.
    Your script should connect to a MySQL server
    running on localhost at port 3306.
    Results must be sorted in ascending order by cities.id
    Results must be display as they are in the example
    below (<state name>: (<city id>) <city name>).
    Your code should not be executed when imported
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, db_name), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    new_state = State(name="California")
    new_city = City(name="San Francisco")
    # appending the city
    new_state.cities.append(new_city)

    rows = session.query(State).order_by(State.id).all()
    for state_row in rows:
        print("{}: {}".format(state_row.id, state_row.name))
        for city_row in state_row.cities:
            print("    {}: {}".format(city_row.id, city_row.name))
    session.close()


if __name__ == "__main__":
    fetch_all()
