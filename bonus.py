marks = int(input("Enter your marks (0-100): "))
if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 45:
    grade = "C"
else:
    grade = "F"
print("Press Enter key to see your teacher's remarks!")
feedback = input({grade})
if grade == "A+":
    feedback = "Excellent! Keep it up."
elif grade == "A":
    feedback = "Very Good!"
elif grade == "B":
    feedback = "Can do much better!"
elif grade == "C":
    feedback = "Poor. Need to improve!"
else:
    feedback = "Very Poor! Call your parents."
print(f"Your grade is: {grade}")
print(f"Teacher's Remarks: {feedback}")