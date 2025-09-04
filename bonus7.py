print("📊 Multiplication Table Generator")

try:
    s, e = int(input("Start: ")), int(input("End: "))
    limit = int(input("Limit: "))
except ValueError:
    print("⚠️ Numbers only!")
    exit()

if s > e: s, e = e, s  # swap if needed

for n in range(s, e + 1):
    print(f"\nTable of {n}:")
    for i in range(1, limit + 1):
        print(f"{n} x {i} = {n*i}")
    print("-" * 20)