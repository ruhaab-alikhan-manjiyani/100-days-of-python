import random
import string

length = int(input("Enter the length of the password: "))
chars = string.ascii_letters + string.digits + string.punctuation
strenght = input("Enter the strength (easy, medium, strong): ").lower()
if strenght == 'easy':
    chars = string.ascii_letters + string.digits
elif strenght == 'medium':
    chars = string.ascii_letters + string.digits
elif strenght == 'strong':
    chars = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid strength level. Using default (strong).")
password = ''.join(random.choice(chars) for _ in range(length))

print("Generated password:", password)