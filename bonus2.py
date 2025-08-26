name = input("What's your name? ")
age = int(input("How old are you? "))
weather = input("What's the weather like? (sunny, cloudy, rainy, snowy, windy) ")
mood = input("How are you feeling today? (happy, sad, tired) ")
if weather == "rainy" and mood == "sad":
    print("Hey! " + name + "Maybe a warm tea & a good book will cheer you up!!")
elif weather == "sunny" and mood == "happy":
    print("🌞 Go out & enjoy the day, " + name + ".")
elif weather == "snowy" and mood == "tired":
    print("How about a power nap 😴!?")
elif weather == "rainy" and mood == "happy":
    print("How about Maggi in this weather!? 🤤")
elif weather == "rainy" and mood == "tired":
    print("Take a power nap!!")
elif weather == "sunny" and mood == "tired":
    print("A power nap is enough to enjoy the day.")
elif weather == "sunny" and mood == "sad":
    print("Nobody's sad when sun is there, go out and look at the nature; it'll cheer you up!")
    