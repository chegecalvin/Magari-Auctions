# lib/cli.py

from functionalities import (
    list_cars,
    create_car,
    find_car_by_id,
    add_car,
    remove_car,
    list_participants,
    find_participant_by_id,
    find_participant_by_name,
    register_participant,
    remove_participant,
    exit_program
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            create_car()
        elif choice == "1":
            list_cars()
        elif choice == "2":
            find_car_by_id()
        elif choice == "3":
            add_car()
        elif choice == "4":
            remove_car()
        elif choice == "5":
            list_participants()
        elif choice == "6":
            find_participant_by_id()
        elif choice == "7":
            find_participant_by_name()
        elif choice == "8":
            register_participant()
        elif choice == "9":
            remove_participant()
        elif choice == "10":
            exit_program()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Create cars")
    print("1. View all cars on auction")
    print("2. Find car by Id")
    print("3. Put up a car for auction")
    print("4. Remove car from auction")
    print("5. View all participants")
    print("6. Find participant by id")
    print("7. Find participant by name")
    print("8. Register participant")
    print("9. Remove participant")
    print("10. Exit program")


if __name__ == "__main__":
    main()
