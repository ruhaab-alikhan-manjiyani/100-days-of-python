print("🧮 Multiplication Table")
limit = int(input("Enter maximum number for the table (eg. 10, 20, 50): "))
print("\n   ", end = "")
for i in range(1, limit + 1):
    print(f"{i:4}", end = "")
print("\n" + "-" * (5 * (limit + 1)))
for i in range(1, limit + 1):
    print(f"{i:2}|", end = "")
    for j in range(1, limit + 1):
        print(f"{i * j:4}", end = "")
    print()