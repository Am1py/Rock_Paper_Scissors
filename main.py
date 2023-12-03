import random
def player_choice():
    while True:
        try:
                player = str(input("Choose rock,paper or scissors: "))
                if player.lower() in ['rock','paper','scissors']:
                    return player.lower()
                else:
                    print("Invalid input. Please enter 'rock','paper','scissors' ")
        except ValueError:
            print("Inalid input. PLease enter a valid string.")

def computer_choise ():
    computer = ['rock','paper','scissors']
    return random.choice(computer)

def winner_decider(computer,user):
    if user == computer:
        return ("\nIt's tie!")
    elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
        return ('\nYou win!')
    else:
        print('\nComputer win!')

def game():
    user = player_choice()
    computer = computer_choise()
    c_score = 0

    print("\nYour choice: "+ user)
    print("Computer choice: "+ computer)
    winner = winner_decider(computer,user)
    print(winner)



game()








