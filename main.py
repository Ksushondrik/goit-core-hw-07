import functions as fu
from classes import AddressBook


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = fu.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(fu.add_contact(args, book))
        elif command == "change":
            print(fu.change_contact(args, book))
        elif command == "phone":
            print(fu.show_phone(args, book))
        elif command == "all":
            print(fu.show_all(book))
        elif command == "add_birthday":
            pass
        elif command == "show_birthday":
            pass
        elif command == "birthdays":
            pass
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
