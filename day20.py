print("📝 Simple Notes App")
while True:
    print("\nOptions: write | read | exit")
    choice = input("Enter Choice: ").lower()

    if choice == "write":
        note = input("Enter your note: ")
        with open("notes.txt", "a") as f:
            f.write(note + "\n")
        print("Note saved.")
    elif choice == "read":
        with open("notes.txt", "r") as f:
            print("\nYour Notes:")
            print(f.read())
    elif choice == "exit":
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")