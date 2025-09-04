from datetime import datetime
print("Advanced Notes App")
while True:
    print("\nOptions: write | read | search | delete | exit")
    choice = input("Choose an option: ").lower()
    if choice == "write":
        note = input("Enter your note: ")
        with open("notes.txt", "a") as f:
            f.write(note+ "\n")
        print("Note added.")
    elif choice == "read":
        try:
            with open("notes.txt", "r") as f:
                notes = f.readlines()
                if notes:
                    for i, note in enumerate(notes, 1):
                        print(f"{i}. {note.strip()}")
                else:
                    print("No notes found.")
        except FileNotFoundError:
            print("No notes found.")
    elif choice == "search":
        keyword = input("Enter keyword to search: ")
        try:
            with open("notes.txt", "r") as f:
                notes = f.readlines()
                found = False
                for i, note in enumerate(notes, 1):
                    if keyword in note:
                        print(f"{i}. {note.strip()}")
                        found = True
                if not found:
                    print("No matching notes found.")
        except FileNotFoundError:
            print("No notes found.")
    elif choice == "delete":
        try:
            with open("notes.txt", "r") as f:
                notes = f.readlines()
                if notes:
                    for i, note in enumerate(notes, 1):
                        print(f"{i}. {note.strip()}")
                    to_delete = int(input("Enter the number of the note to delete: "))
                    if 1 <= to_delete <= len(notes):
                        del notes[to_delete - 1]
                        with open("notes.txt", "w") as f:
                            f.writelines(notes)
                        print("Note deleted.")
                    else:
                        print("Invalid number.")
                else:
                    print("No notes to delete.")
        except FileNotFoundError:
            print("No notes found.")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "exit":
        print("Exiting the app.")
        break