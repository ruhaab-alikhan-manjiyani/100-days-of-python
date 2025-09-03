import random
from datetime import datetime
print("🎲 Dice Game [2 Players]")

player1_score = 0
player2_score = 0
target = 5

while True:
    roll1 = input("Player 1, Roll Dice? (yes/no): ").lower()
    if roll1 == 'yes':
        num1 = random.randint(1, 6)
        player1_score += num1
        print(f"Player 1 rolled {num1} at {datetime.now().strftime('%H:%M:%S')}")
        print(f"Player 1's total score: {player1_score}")
    elif roll1 == 'no':
        print("Player 1 quit. Game Over!")
        break

    roll2 = input("Player 2, Roll Dice? (yes/no): ").lower()
    if roll2 == 'yes':
        num2 = random.randint(1, 6)
        player2_score += num2
        print(f"Player 2 rolled {num2} at {datetime.now().strftime('%H:%M:%S')}")
        print(f"Player 2's total score: {player2_score}")
    elif roll2 == 'no':
        print("Player 2 quit. Game Over!")
        break

    if player1_score >= target:
        print("🏆 Player 1 wins!")
        break
    elif player2_score >= target:
        print("🏆 Player 2 wins!")
        break