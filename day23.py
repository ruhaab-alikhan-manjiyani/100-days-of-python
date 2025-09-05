print("📝 Student Grades Analyzer")
grades_input = input("Enter grades (seperated by comma): ")
grades = [int(x.strip()) for x in grades_input.split(",") if x.strip().isdigit()]
def average(lst):
    return sum(lst) / len(lst) if lst else 0
def highest(lst):
    return max(lst) if lst else None
def lowest(lst):
    return min(lst) if lst else None

print("\n📊 Results:-")
print("Average: ", round(average(grades), 2))
print("Highest: ", highest(grades))
print("Lowest: ", lowest(grades))