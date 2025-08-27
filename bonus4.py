print("🛒 Grocery List Manager")

groceries = []

while True:
    item = input("Add an item (or type 'done' to finish): ")
    if item.lower() == "done":
        break
    groceries.append(item)

print("\n📝 Your Grocery List:")
for i, item in enumerate(groceries, 1):
    print(f"{i}. {item}")
print("\nThank you for using the Grocery List Manager!")