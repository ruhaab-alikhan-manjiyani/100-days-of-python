print(" 🛒 Grocery List Manager")

groceries = []

while True:
    print("\nOptions:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Clear list")
    print("5. Save & Exit")
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        item = input("Enter item to add: ")
        groceries.append(item)
        print(f"✅ {item} added.")

    elif choice == '2':
        item = input("Enter item to remove: ")
        if item in groceries:
            groceries.remove(item)
            print(f"❌ {item} removed.")
        else:
            print(f"⚠️ {item} not found in the list.")

    elif choice == '3':
        if groceries:
            print("📝 Grocery List:")
            for idx, item in enumerate(groceries, 1):
                print(f"{idx}. {item}")
        else:
            print("🛒 Your grocery list is empty.")

    elif choice == '4':
        groceries.clear()
        print("🗑️ Grocery list cleared.")

    elif choice == '5':
        with open("grocery_list.txt", "w") as file:
            for item in groceries:
                file.write(f"{item}\n")
        print("💾 Grocery list saved. Exiting...")
        break

    else:
        print("❗ Invalid choice. Please select a valid option.")