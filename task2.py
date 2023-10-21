def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list[str], contacts: dict[str, str]):
    name, phone = args
    if name in contacts:
        return "A contact with that name already exists. If you want to change a contact, use the \"change\" command."

    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]):
    name, phone = args
    if name not in contacts:
        return "A contact with that name doesn't exist. If you want to add a new contact use the \"add\" command."

    contacts[name] = phone
    return "Contact changed."


def show_phone(args: list[str], contacts: dict[str, str]):
    name, = args
    if name not in contacts:
        return "A contact with that name doesn't exist."

    return contacts[name]


def main():
    contacts: dict[str, str] = {}

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
                print(show_phone(args, contacts))
            elif command == "all":
                print("|{:^20}|{:^20}|".format('Contact name', 'Phone number'))
                for contact_name, phone in contacts.items():
                    print("|{:^20}|{:^20}|".format(contact_name, phone))
            else:
                print("Invalid command.")
        except:
            print('Oops, something went wrong. Please check your input and try again.')


if __name__ == "__main__":
    main()
