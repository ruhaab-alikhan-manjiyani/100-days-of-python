print("Let's play Mad Libs!")
name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb (past tense): ")

# Final Story Output
story = f"""
Once upon a time, {name} went to {place}.
There, {name} saw a very {adjective} {animal}!
{name} {verb} as fast as {name} could, and enjoyed alot.
"""

print("\n Your Mad Libs Story: ")
print(story)

print("Coded by Ruhaab!")