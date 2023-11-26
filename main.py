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







