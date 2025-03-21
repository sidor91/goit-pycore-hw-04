import re

validate_phone_error_msg = "The phone should optionally contain country code (1-3 digits with/withount +) " \
"and mandatory contain a regional code (1-4 digits with/without brackets()) followed by up to 9 digits. " \
"Allowed separators are ' ', '-', '.'"

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list[str], contacts: dict):
    if len(args) < 2:
        return (
            '"add contact" command should contain 2 arguments "name" and "phone number"'
        )
    elif not args[0].isalpha():
        return "name must consist of letters only"
    elif not is_valid_phone(args[1]):
        return validate_phone_error_msg
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args: list[str], contacts: dict):
    if len(args) < 2:
        return (
            '"change contact" command should contain 2 arguments "name" and "phone number"'
        )
    elif not contacts.get(args[0]):
        return f"Contact with name {args[0]} was not found"
    elif not is_valid_phone(args[1]):
        return validate_phone_error_msg

    name, phone = args
    contacts[name] = phone
    return "Contact changed."

def get_contact(args: list[str], contacts: dict):
    if len(args):
        return contacts.get(args[0], "User not found")
    else:
        return "Contact name missing"


def is_valid_phone(phone):
    pattern = r"^\+?\d{1,3}?[-.\s]?(\(\d{1,4}\)|\d{1,4})[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
    return bool(re.fullmatch(pattern, phone))


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(get_contact(args, contacts))
            elif command == "all":
                print(contacts)
            else:
                print("Invalid command.")
        except ValueError:
            print("There are no arguments passed")


if __name__ == "__main__":
    main()
