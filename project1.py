import random

meals = {
    "breakfast": ["Oats with milk", "Poha", "Paratha", "Smoothie", "Eggs & Toast", "Idli", "Upma"],
    "lunch": ["Dal & Rice", "Rajma & Rice", "Chole & Roti", "Pasta", "Vegetable Pulao", "Curd Rice"],
    "dinner": ["Paneer Curry & Roti", "Fried Rice", "Soup & Bread", "Khichdi", "Veg Biryani", "Maggi"],
}

def generate_meal_plan(preferences=None):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    plan = {}

    for day in days:
        plan[day] = {
            "Breakfast": random.choice(meals["breakfast"]),
            "Lunch": random.choice(meals["lunch"]),
            "Dinner": random.choice(meals["dinner"])
        }

    return plan

def display_plan(plan):
    print("\nWeekly Meal Plan:\n" + "-"*25)
    for day, meals in plan.items():
        print(f"\n{day}:")
        for meal_type, dish in meals.items():
            print(f"  {meal_type}: {dish}")

meal_plan = generate_meal_plan()
display_plan(meal_plan)