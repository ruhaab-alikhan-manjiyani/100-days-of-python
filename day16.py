print("Contact Book")
contacts={}
while True:
    print("\nOptions: add | view | search | remove | exit")
    choice=input("Choose an option: ").lower()
    if choice=="add":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(f"Contact {name} added.")
    elif choice=="view":
        if contacts:
            print("Contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")
    elif choice=="search":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print(f"Contact {name} not found.")
    elif choice=="remove":
        name = input("Enter name to remove: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} removed.")
        else:
            print(f"Contact {name} not found.")
    elif choice=="exit":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid option. Please try again.")