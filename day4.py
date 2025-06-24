print("🧮 BMI Calculator")
weight = float(input("Enter your weight in kg: "))
feet = int(input("Enter your height (feet): "))
inches = int(input("Enter your remaining height (inches): "))
#Convert height to meters
total_inches = feet * 12 + inches
height_m = total_inches * 0.0254 # 1 inch = 0.0254 meters
# Calculate BMI
bmi = weight / (height_m ** 2)
print(f"Your BMI is: {round(bmi, 2)}")
# Categorize BMI
if bmi < 18.5:
    print("🟡 You're underweight.")
elif 18.5 <= bmi < 25:
    print("🟢 You're healthy.")
elif 25 <= bmi < 30:
    print("🟠 You're overweight.")
else:
    print("🔴 You're obese.")