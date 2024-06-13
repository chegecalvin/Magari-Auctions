#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.cars import Car
from models.participant import Participant

def sample_database():
    Car.create_table()
    Participant.create_table()

    BMW=Car.add_car("BMW X6",2018,2000000)
    Mercedes=Car.add_car("GLE 63",2019,10000000)
    Participant.add_participant("Calvin",18,"Thika",1)
    Participant.add_participant("Kevin",20,"Nairobi",2)
    Participant.add_participant("Nicole",25,"South B",1)
    Participant.add_participant("Melissa",40,"Kitengela",2)

sample_database()
print("Sample data")