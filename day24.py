import random
choices = ['rock', 'paper', 'scissors']
player_input = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(choices)
print(f"Computer chose: {computer}")
if player_input == computer:
    print("It's a tie!")
elif (player_input == 'rock' and computer == 'scissors') or \
     (player_input == 'paper' and computer == 'rock') or \
     (player_input == 'scissors' and computer == 'paper'):
    print("🎉 You win!")
else:
    print("🖥️ Computer Wins!")
