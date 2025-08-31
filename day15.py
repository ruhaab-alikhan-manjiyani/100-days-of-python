def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "Error! Division by zero."
    return a/b
def power(a,b):
    return a**b
def modulus(a,b):
    return a%b
def floor_divide(a,b):
    if b == 0:
        return "Error! Division by zero."
    return a//b
def calculator():
    print("Advanced Python Calculator")
    print("Operations: +, -, *, /, **, %, //")
    print("Type 'exit' to quit")
    while True:
        op = input("Enter operation: ")
        if op == 'exit':
            print("Exiting calculator.")
            break
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        if op == '+':
            print(f"Result: {add(a,b)}")
        elif op == '-':
            print(f"Result: {subtract(a,b)}")
        elif op == '*':
            print(f"Result: {multiply(a,b)}")
        elif op == '/':
            print(f"Result: {divide(a,b)}")
        elif op == '**':
            print(f"Result: {power(a,b)}")
        elif op == '%':
            print(f"Result: {modulus(a,b)}")
        elif op == '//':
            print(f"Result: {floor_divide(a,b)}")
        elif op == '**':
            print(f"Result: {power(a,b)}")
        else:
            print("Invalid operation. Please try again.")
        print("-"*30)

        calculator()