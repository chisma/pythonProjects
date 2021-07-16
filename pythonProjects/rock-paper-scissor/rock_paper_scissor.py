import random


def play(player):
    if(player == '' or (player != 'r' and player != 'p' and player != 's')):
        return 'x'
    computer = random.choice(['r', 'p', 's'])
    print(game_play(player, computer))


def game_play(player, computer):
    # Is no input or invalid input-> exit game
    if(player == '' or (player != 'r' and player != 'p' and player != 's')):
        return "Invalid input!Try again!"
    # r > s, p > r, s > p
    if (player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer == 'p'):
        return f"You won!!!\nComputer played {computer}!"

    elif (player == 'r' and computer == 'p') or (player == 'p' and computer == 's') or (player == 's' and computer == 'r'):
        return f"You lost!!!\n\\\\\\\\Computer played {computer}!\\\\\\\\"

    else:
        return f"It's a tie!!!Computer also played {computer}!"


if __name__ == "__main__":
    print("*******ROCK  -  PAPER   -  SCISSORS********")
    input("Hit ENTER to PLAY!")
    player = 'x'
    while(player == 'x'):
        player = input("Rock, Paper or Scissors?(r/p/s)? ").lower()
        if play(player) == 'x':
            print("Invalid input, try again!")
            player = 'x'
