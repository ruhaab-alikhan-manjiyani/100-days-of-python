num = int(input("Enter a number: "))
print(f"\n📊 Multiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")