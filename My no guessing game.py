"""
Multiplayer Number Guessing Game

Author: Lloyd Aboulnaja
Description: A console-based multiplayer number guessing game 
featuring input validation and structured testing documentation.
"""



import random


def exit_menu():
    print("\nThanks for playing!!. See you next time!!.")
    exit_button = input("Press the [ENTER] button on the keyboard to EXIT...")
    quit()
   
def start():
    player_counter = num_players
    while True:
        names_entry = input(f"Enter {player_counter} names of players: ")
        if names_entry == "":
            print("Name cannot be blank!. Try again.")
        elif names_entry.isdigit():
            print("The names entered cannot be a number!. Try again.")
        elif len(names_entry) < 2 or len(names_entry) > 15:
            print("Invalid name!.")
        else:
            name_list.append(names_entry)
            player_counter = player_counter - 1
        if player_counter == 0:
            print(f"The players are: {name_list}.")
            break

def main_menu(): #Main menu interface
    global num_players
    global name_list
    print("\n=======================================")
    print("== WELCOME TO A NUMBER GUESSING GAME ==")
    print("======= 1.[PLAY] 2.[EXIT] =============")
    print("=======================================")
    while True:
      main_menu = input("Make a choice from the options above (1-2): ")
      if main_menu.strip() == "":
          print("Your choice cannot be blank!. Try again")
      elif main_menu not in ["1","2"]:
          print("Invalid choice!. Try again.")
      elif not main_menu.isdigit():
          print("Your choice must be a number!. Try again.")
      elif main_menu == "2":
          exit_menu()
      elif main_menu == "1":
          name_list = []
          flag = True
          while flag:
            try:
                no_players = int(input('''Enter number of players to play the game: '''))
            except ValueError:
                print("Invalid value!. Try again.")
                continue
            num_players = no_players
            if num_players > 10 or num_players <= 0:
                print('''Invalid value!. The number of players must be from 1 to 10 (1-10).''')
                continue
            else:
                print("Number of players accepted!.")
            flag = False
            start()
            play()
           
def after_play(): # Displays when player wins or out of guesses
    print("1. Continue (Play Again) \n2. Exit \n3. Main menu")
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid choice!. Try again")
            continue
        if choice == 1:
            play()
        elif choice == 2:
            exit_menu()
        elif choice == 3:
            main_menu()
        else:
            print("Invalid choice!. Try again")
            break

def play():

    random_num = random.choice(list(range(1,50)))
    game_won = False  
   
    print("\nI am thinking of a number from 1 to 50.")
    for i in name_list:

        if len(name_list) > 1:
            print(f"\n[NOTE]: Each player has 3 guesses. {i}'s turn!")
            guesses = 3
        else:
            print(f"\n[NOTE]: You have 5 chances, {i}!")
            guesses = 5
           
       
        while guesses > 0:
            try:
                user_guess = int(input(f"({guesses} left) Enter guess: "))
            except ValueError:
                print("Invalid value! Enter a number.")
                continue
            if user_guess > 50 or user_guess <= 0:
                print("Your guess is out of range!.")
            elif user_guess > random_num:
                print("Too high!")
                guesses = guesses - 1
            elif user_guess < random_num:
                print("Too low!")
                guesses = guesses - 1
            else:
                print(f"CONGRATS! {i} guessed correctly!")
                game_won = True
                after_play()
       
        if game_won:
            break
       
    if not game_won:
        print(f"\nNobody won! The number was {random_num}.")
        after_play()
       
               
main_menu()             