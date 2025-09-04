shopping = []
print("🛒 Shopping List App")

while True:
    print("\nOptions: add | view | search | remove | clear | exit")
    choice = input("Choose an option: ").lower()

    if choice == "add":
        item = input("Enter item to add: ")
        shopping.append(item)
        print(f"✅ {item} added to the list.")

    elif choice == "view":
        print("\n🛍️ Shopping List:")
        for i, item in enumerate (shopping, start=1):
            print(f"{i}. {item}")

    elif choice == "search":
        item = input("Enter item to search: ")
        if item in shopping:
            print(f"🔍 {item} is in the list.")
        else:
            print(f"❌ {item} not found in the list.")

    elif choice == "remove":
        item = input("Enter item to remove: ")
        if item in shopping:
            shopping.remove(item)
            print(f"🗑️ {item} removed from the list.")
        else:
            print(f"❌ {item} not found in the list.")

    elif choice == "clear":
        shopping.clear()
        print("🧹 Shopping list cleared.")

    elif choice == "exit":
        print("👋 Exiting . . . .")
        break

    else:
        print("❗ Invalid option. Please try again.")