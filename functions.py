import decor as de
from classes import AddressBook, Record


def parse_input (user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@de.input_error
def add_contact (args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@de.input_error
def change_contact(args, book: AddressBook):
    name, phone, new_phone, *_ = args
    record = book.find(name)
    if isinstance(record, Record):
        record.edit_phone(phone, new_phone)
        return "Contact updated."
    else:
        raise Exception("Not found!")


@de.input_error
def show_phone (args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if isinstance(record, Record):
        return record
    else:
        raise Exception("Not found!")


@de.input_error
def show_all(book: AddressBook):
    if len(book) > 0:
        for name, record in book.data.items():
            print(record)
        return f"It's all"
    else:
        raise Exception("No mach to show!")
