weather = input("How's the weather like today? (sunny, rainy, cloudy, snowy, storm, windy): ").lower()
if weather == "rainy":
    print("☔ Don't forget your umbrella.")
elif weather == "cloudy":
    print("Might rain, carry an umbrella just in case 🌥️☂️")
elif weather == "sunny":
    print("☀️ Apply sunscreen & enjoy the day!")
elif weather == "snowy":
    print("Stay warm and make a snowman ☃️")
elif weather == "windy":
    print("Let the lighter people stay in, to be safe 🌬️🍃")
elif weather == "storm":
    print("Oops, make sure you in a safe place right now 😶‍🌫️")
else:
    print("I am not sure what that means, look outside & tell me!!")