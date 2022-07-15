# Introduction to the game
print("""                                                       
                                                ████                                
                                    ██    ██████████                                  
                                    ██  ██▒▒▒▒▒▒▒▒██                                  
                                  ██████▒▒▒▒▒▒▒▒▒▒██                                  
                                  ██  ██▒▒▒▒▒▒▒▒██                                    
                                ██    █████████                                      
                              ██    ██                                            
                              ██    ██                                            
                            ██        ███                                         
                          ██              ████████████                                 
                    ████████████        ██▒▒▒▒▒▒▒▒▒▒▒▒▒██                                
                  ██▒▒▒▒▒▒▒▒▒▒▒▒██    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                              
                ██▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒██  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                              
                ██▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒██  ██▒▒  ▒▒▒▒▒▒▒▒▒▒▒▒██                              
                ██▒▒▒▒▒▒▒▒▒▒▒▒  ▒▒██  ██▒▒▒▒    ▒▒▒▒▒▒▒▒██                              
                ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    ██▒▒▒▒▒▒▒▒▒▒▒▒██                                
                  ██▒▒▒▒▒▒▒▒▒▒▒▒██        ████████████                                  
                    ████████████           
""")
print("*" * 80)
print("\n", " " * 27, "WELCOME TO MASTERMIND!", "\n")
print("*" * 80)
print("\nThere are 5 kinds of fruits in this game.")
print("The 5 fruits are 'CHERRY', 'GRAPE', 'APPLE', 'APRICOT', 'PEAR'.")
print("\nOut of these 5 fruits, 4 fruits will randomly chosen and placed in a list.")
print("Try to guess the correct position and type of fruit that will appear!")
print("\nHINT: There may be a repetition of the same fruit in the list.\n")

# This is the list of the fruits that will be used in this game.
main_fruit_list = ['CHERRY', 'GRAPE', 'APPLE', 'APRICOT', 'PEAR']


# Generating a random list of fruits from the main list of fruits.
def rand_fruits():
    import random
    generated_fruit_list = random.sample(main_fruit_list, k=4)
    return generated_fruit_list


# Defining Option 1 of the Game; Consists of the entire game's mechanics.
def option1():
    print("\n", "-" * 80)
    print("\nThis is the list of fruits that are available in this game: \n", main_fruit_list)
    print("\nA list of 4 random fruits will be generated using the fruits from that main list.")
    print("HINT: There may be a repetition of the same fruit in the list.\n")
    print("You have 3 ATTEMPTS to guess the fruits!")
    print("\n", "-" * 35, " BEGIN! ", "-" * 35)
    rand_fruits_list = rand_fruits()
    # Printing the randomly generated list for demo purposes of the game.
    print("\nThis is the random-generated list: ", rand_fruits_list)
    print("The list above is shown for purely DEMONSTRATION purposes.")
    print("In the real game, this list will not be shown.\n")
    main_player_guesses = []
    attempts = 0
    while attempts < 3:
        correct_fruit = 0
        correct_position = 0
        wrong_position = 0
        # Only the fruits that belong in the main list are allowed to be chosen by the user.
        while len(main_player_guesses) != 4:
            player_guesses = str(input("Enter the fruit that might appear in the list: ").upper())
            if player_guesses == 'CHERRY':
                main_player_guesses.append(player_guesses)
            elif player_guesses == 'GRAPE':
                main_player_guesses.append(player_guesses)
            elif player_guesses == 'APPLE':
                main_player_guesses.append(player_guesses)
            elif player_guesses == 'APRICOT':
                main_player_guesses.append(player_guesses)
            elif player_guesses == 'PEAR':
                main_player_guesses.append(player_guesses)
            else:
                print("ERROR: Please enter the fruits from the main list or make sure your spelling of it is correct!")
                print("The main fruit list is", main_fruit_list, "\n")
        attempts += 1
        print("\nYOUR GUESS IS:\n", main_player_guesses)
        if main_player_guesses == rand_fruits_list:
            # If the player guesses correctly at any time.
            print("\n", "*" * 80)
            print("\n", " " * 33, " VICTORY! ", " " * 33)
            print(" " * 13, "You guessed the fruits correctly with only", attempts, "attempt!\n")
            print("*" * 80)
            break
        else:
            # If the player guesses wrongly, the player's list is checked and hints are given to improve guessing.
            for i in range(4):
                if main_player_guesses[i] == rand_fruits_list[i]:
                    correct_fruit += 1
                if main_player_guesses[i] == rand_fruits_list[i]:
                    correct_position += 1
                if main_player_guesses[i] in rand_fruits_list and main_player_guesses[i] != rand_fruits_list[i]:
                    wrong_position += 1
            print("You guessed", correct_fruit, "fruits correctly.")
            print("Out of these correct fruit guesses,", correct_position, "fruits were in the right position.")
            print("Out of these correct fruit guesses,", wrong_position, "fruits were in the wrong position.")
        print("This is your", attempts, "attempt.\n")
        # The player's list is emptied at the end of each guess to fill in 4 new guesses.
        main_player_guesses.clear()
        if attempts == 3:
            print("*" * 80)
            print("\n", " " * 32, " GAME OVER! ", " " * 32)
            print("\n", "-" * 80)
            print("\nYou failed to guess the correct fruits!")
            print("This was the correct answer: ", rand_fruits_list, "\n")
            print("*" * 80)


# Defining Option 2 for the main menu section of the game.
def option2():
    print("\n", "To play this game, you will be asked to input 4 fruits of your choice into a list.")
    print("The game shall then check if your fruit choices and the position of it is correct.", "\n")
    print("If your fruit choices are wrong, the game will give you some hints to aid your future guesses.")
    print("Eg. 'Out of these correct fruit guesses, 2 fruits were in the right position.'")
    print("HINT: There may be a repetition of the same fruit in the list.\n")
    print("HAPPY GUESSING!\n")


# Defining Option 3 for the main menu section of the game.
def option3():
    print("\n", "*" * 80, "\n")
    print(" " * 27, "THANK YOU FOR YOUR TIME!", "\n")
    print("*" * 80)


# Defining the main menu prompt.
def main_menu():
    main_menu_option = True
    while main_menu_option:
        print("\n", "*" * 80)
        print("\n", "-" * 33, " MAIN MENU ", "-" * 33, "\n")
        print("*" * 80)
        print("\n[1] PLAY")
        print("[2] HOW TO PLAY")
        print("[3] QUIT", "\n")
        main_menu_option = input("ENTER YOUR CHOICE! \n[1/2/3]: ")
        if main_menu_option == "1":
            option1()
            main_menu()
            main_menu_option = False
        elif main_menu_option == "2":
            option2()
            main_menu()
            main_menu_option = False
        elif main_menu_option == "3":
            option3()
            main_menu_option = False
        else:
            print("ERROR: Please enter 1, 2 or 3 only!\n")


# giving user the option if they'd like to play
play_option = True
while play_option:
    play = str(input("WOULD YOU LIKE TO PLAY? [Y/N] ").upper())
    if play == "Y":
        main_menu()
        play_option = False
    elif play == "N":
        option3()
        play_option = False
    else:
        print("\n", "ERROR, INPUT IS NOT RECOGNIZED. PLEASE ENTER Y OR N ONLY.", "\n")
