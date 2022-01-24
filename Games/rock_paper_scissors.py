import random

def play():
    user = input("Please Choice ('r' for rock, 'p' fr paper, 's' scissors)\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You Won!!!'
    else:
        return 'You Lost!!!'

# Rules: r > s, s > p, p > r

def is_win(player, opponent):
    if (player == 'r' and c == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())