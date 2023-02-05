import random


def play():
    user = input("(R) for rock, (P) for paper or (S) for scissors. Enter your choice: ").lower()
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        print('It is a tie! You both choose the same thing!')
        return play()

    if you_win(user, computer):
        return 'YOU WON!'

    print('YOU LOST!')
    return play()


def you_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (
            player == 'p' and computer == 'r'):
        return True

print(play())