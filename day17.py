print("🎓 Student Marks Tracker")
students = []
while True:
    print("\nOptions: add | view | exit")
    choice = input("Enter choice: ").lower()
    if choice == "add":
        name = input("Enter student name: ")
        marks = input("Enter student marks: ")
        students.append({"name": name, "marks": marks})
        print(f"✅ Added {name} with marks {marks}.")
    elif choice == "view":
        if students:
            print("\n📋 Student List:")
            for s in students:
                print(f" - {s['name']}: {s['marks']}")
        else:
            print("📪 No students added yet.")
    elif choice == "exit":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice, please try again.")