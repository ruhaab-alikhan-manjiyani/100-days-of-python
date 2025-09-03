print("🎓 Student Marks Tracker Pro")

students = []

while True:
    print("\nOptions: add | view | topper | exit")
    choice = input("Enter choice: ").lower()

    if choice == "add":
        name = input("Enter student name: ")

        # subject-wise marks
        math = int(input("Enter Math marks: "))
        cs = int(input("Enter CS marks: "))
        business = int(input("Enter Business marks: "))

        # calculate average
        avg = (math + cs + business) / 3

        students.append({
            "name": name,
            "marks": {
                "Math": math,
                "CS": cs,
                "Business": business
            },
            "average": avg
        })

        print(f"✅ Added {name} with average {round(avg,2)}")

    elif choice == "view":
        if students:
            print("\n📊 Student List:")
            for s in students:
                print(f"\n{s['name']} → Average: {round(s['average'],2)}")
                for subject, marks in s["marks"].items():
                    print(f"   {subject}: {marks}")
        else:
            print("📭 No students yet!")

    elif choice == "topper":
        if students:
            topper = max(students, key=lambda s: s["average"])
            print(f"\n🏆 Topper: {topper['name']} with avg {round(topper['average'],2)}")
        else:
            print("📭 No students yet!")

    elif choice == "exit":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice")