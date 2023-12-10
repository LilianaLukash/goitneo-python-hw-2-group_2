def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."       
        except KeyboardInterrupt:
            return "Program stopped by user"
    return inner

# checking if the contact exist
def input_error_ifexistcontact(func):
    def inner(args, contacts):
        name, phone = args
        if name in contacts:
            return "Contact already exist"
        else:
            return func(args, contacts)
    return inner

def input_error_ifexistphone(func):
    def inner(args, contacts):
        name, phone = args
        # checking if the phone exist
        for contact_name, contact_phone in contacts.items():
            if phone == contact_phone:
                if name == contact_name:
                    return f"This phone already belongs to {name}"
                else:
                    return f"This phone number is already used by {contact_name}."
        return func(args, contacts)       
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error_ifexistcontact
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error_ifexistphone
@input_error
def change_username_phone(args, contacts):
    # update existing phone in the list
    name, phone = args
    contacts[name] = phone
    return f"Phone of {name} changed to {phone}"
 
def phone_username(args, contacts):
    # return phone from username
    username = args
    return contacts[username]    

def all(contacts):
    # return all contacts and phones
    contacts_list = [f"{name} {phone}" for name, phone in contacts.items()]
    contacts_line = "\n".join(contacts_list)
    return contacts_line

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
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
            print(change_username_phone(args, contacts))
        
        elif command == "all":
            print(all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()