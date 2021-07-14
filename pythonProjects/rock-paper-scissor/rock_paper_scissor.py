import random


def play():
    print("Are you ready to play Rock-Paper-Scissors with the computer?")
    input("Hit ENTER to PLAY!")
    player = input("Rock, Paper or Scissors?(r/p/s)? ").lower()
    computer = random.choice(['r', 'p', 's'])
    game_play(player, computer)


def game_play(player, computer):
    # r > s, p > r, s > p
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        print(f"You won!!!\nComputer played {computer}!")

    elif (player == 'r' and computer == 'p') or (player == 'p' and computer == 's') or (player == 's' and computer == 'r'):
        print(f"You lost!!!\n\\\\\\\\Computer played {computer}!\\\\\\\\")

    else:
        print(f"It's a tie!!!Computer also played {computer}!")


play()
