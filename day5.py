print("🧮 Basic Python Calculator")
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /, //, %, **): ")
num2 = float(input("Enter second number: "))
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "⚠️ Cannot divide by zero!"
elif op == "//":
    if num2 != 0:
        result = num1 // num2
    else:
        result = "⚠️ Cannot floor divide by zero!"
elif op == "%":
    if num2 != 0:
        result = num1 % num2
    else:
        result = "⚠️ Cannot find remainder with zero!"
elif op == "**":
    result = num1 ** num2
else:
    result = "❌ Invalid operator!"
print(f"Result: {result}")