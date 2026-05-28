from colorama import Fore, init

init(autoreset=True)


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def is_valid_phone(phone):
    if not phone.startswith("+"):
        return "Phone number must start with +"
    if not phone[1:].isdigit():
        return "Phone number must contain only digits."
    return True


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please provide both name and phone number."
        except IndexError:
            return "Enter user name."
        except KeyError:
            return "Contact not found."
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f"Contact {name} already exists."

    validation = is_valid_phone(phone)
    if validation is not True:
        return validation

    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}."


@input_error
def change_contact(args, contacts):
    name, phone = args
    validation = is_valid_phone(phone)
    if validation is not True:
        return validation

    if name not in contacts:
        return f"Contact {name} not found."
    contacts[name] = phone
    return f"Contact {name} updated with new phone number {phone}."


@input_error
def show_contact(args, contacts):
    name = args[0]
    if name not in contacts:
        return f"Contact {name} not found."
    return f"{name}: {contacts[name]}"


@input_error
def show_all_contacts(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return "No contacts found."


def main():
    contacts = {}  # просто словник, без файлу

    print(Fore.CYAN + "Welcome to the assistant bot!")
    print(Fore.GREEN + "Available commands: \n-> hello \n-> add <name> <phone> \n-> change <name> <phone> \n-> phone <name> \n-> all \n-> close/exit")

    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.YELLOW + "Good bye!")
            break
        elif command == "hello":
            print(Fore.GREEN + "How can I help you?")
        elif command == "add":
            print(Fore.GREEN + add_contact(args, contacts))
        elif command == "change":
            print(Fore.GREEN + change_contact(args, contacts))
        elif command == "phone":
            print(Fore.GREEN + show_contact(args, contacts))
        elif command == "all":
            print(Fore.GREEN + show_all_contacts(contacts))
        else:
            print(Fore.RED + "Invalid command.")


if __name__ == "__main__":
    main()
