from models.cars import Car
from models.participant import Participant

def create_car():
    Car.create_table()
    print("Car table created.")

def list_cars():
    cars = Car.get_all_cars()
    for car in cars:
        print(car)

def find_car_by_id():
    try:
        id_ = int(input("Enter car id: "))
        car = Car.get_by_id(id_)
        print(car) if car else print("Car id not found")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")

def add_car():
    try:
        make = input("Enter car make: ")
        manufacture_yr = int(input("Enter car's year of manufacture: "))
        price = int(input("Enter car's price: "))
        car = Car.add_car(manufacture_yr, make, price)
        print(f'Success: {car}')
    except ValueError as ve:
        print("Error: ", ve)
    except Exception as exc:
        print("Error: ", exc)

def remove_car():
    try:
        id_ = int(input("Enter car's id: "))
        car = Car.get_by_id(id_)
        if car:
            car.delete_car()
            print("Car successfully removed")
        else:
            print("Error: Car not found")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")

def list_participants():
    participants = Participant.get_all_participants()
    for participant in participants:
        print(participant)

def find_participant_by_id():
    try:
        id_ = int(input("Enter participant's id: "))
        participant = Participant.get_by_id(id_)
        print(participant) if participant else print("Participant not found")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")

def find_participant_by_name():
    name = input("Enter participant's name: ")
    participant = Participant.find_by_name(name)
    print(participant) if participant else print("Participant not found")

def register_participant():
    name = input("Enter participant's name: ")
    age = int(input("Enter participant's age: "))
    location = input("Enter participant's location: ")
    car_id = int(input("Enter car id: "))
    try:
        participant = Participant.add_participant(name, age, location, car_id)
        print(f'Success: {participant}')
    except ValueError as ve:
        print("Error: ", ve)
    except Exception as exc:
        print("Error: ", exc)

def remove_participant():
    try:
        id_ = int(input("Enter participant's id: "))
        participant = Participant.get_by_id(id_)
        if participant:
            participant.remove_participant()
            print("Participant successfully removed")
        else:
            print("Error: Participant not found")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")

def exit_program():
    print("Thank you!")
    exit()
