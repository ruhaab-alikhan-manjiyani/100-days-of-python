score = 0
print("🎯 Welcome to the Quiz Game!")

q1 = input("1. What is the capital of France?\nYour answer: ")
if q1.lower() == "paris":
    score += 1
    print("✅ Correct!")
else:
    print("❌ Incorrect!")

q2 = input("2. How many hearts does an octopus have?\nYour answer: ")
if q2 == "3":
    score += 1
    print("✅ Correct!")
else:
    print("❌ Incorrect!")

q3 = input("3. What is the national animal of Australia?\nYour answer: ")
if q3.lower() == "kangaroo":
    score += 1
    print("✅ Correct!")
else:
    print("❌ Incorrect!")

print(f"🏆 Your total score is: {score}/3")