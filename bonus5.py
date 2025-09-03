import random

print("🎲 Dice Roller")
while True:
    roll = input("Roll the dice? (yes/no): ").lower()
    if roll == "yes":
        print("You rolled:", random.randint(1,6))
    elif roll == "no":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Type yes or no")