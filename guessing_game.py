import random     # Imports the random module to create random number for guessing.

high_score = None     # Created a variable to track the score through the loops and the value is set to none for updating it with a condition to match the lowest attempts.

def start_game():     # Created a function to store the game and start it when called.

    global high_score     # Keeping the variable global to update the value along the way, not just in one loop.

    print('----------------------- Welcome to the number guessing game------------------')

    while True:     # While loop for the user to guess the number again if incorrect response.
        try:
            number_picked = int(input('Guess a number between 1  - 10 : '))
            attempts = 1
            break
             
        except ValueError as err: print('Please enter a Valid integer PTA')
        

    guessed_num = random.randrange(11)     #random range used to select a random number and store it guessed_num variable

    while number_picked != guessed_num:     #  while Condition to check the guess is correct and to prompt the user to keep guessing till the time they win.
            
            if number_picked > 10:          # if statements to highlight how close the guess is and to inform the user in case any incorrect input
                print('That is out of the given range guess a number between (1 - 10)')    

            elif number_picked > guessed_num:
                print('That is higher')  

            elif number_picked < guessed_num:
                print('That is a little lower')  

              
            try:                                                 # try block to capture in valid inputs. 
                number_picked  = int(input('Guess again  '))
                attempts += 1
            except ValueError: print('Please Enter a Valid  integer')

            
    print(f'Great you got it!! It took you {attempts} tries')

    if high_score is None or attempts < high_score:     #Condition to update the high_score with the lowest attempts count.
         high_score = attempts                         #updating the high_score as attempts if the above condition meets.
    
    print(f'The HIGH SCORE is {high_score}, CAN YOU BEAT THAT?')

    play_again = input('Awesome, would you like to play again? [y]es/[n]no: ')      # Confirmation for playing the game again.
    while play_again.lower() == 'y':                                          # Starting the game loop again if y as yes.

        
        while True:
            try:
                number_picked = int(input('Guess a number between 1  - 10 : '))
                attempts = 1
                break
            except ValueError as err: print('Please enter a Valid integer PTA')
        

        guessed_num = random.randrange(11)

        while number_picked != guessed_num:
                
                if number_picked > 10:
                    print('That is out of the give range, please enter a number between(1 - 10)')

                elif number_picked > guessed_num:
                    print('That is higher')    

                elif number_picked < guessed_num:
                    print('That is a little lower')

                
                try:
                    number_picked  = int(input('Guess again  '))
                    attempts += 1
                except ValueError: print('Please Enter a Valid  integer')

            
        print(f'Great you got it!! It took you {attempts} tries')

        if high_score is None or attempts < high_score:
         high_score = attempts
    
        print(f'The HIGH SCORE is {high_score}, can you beat that?')

        play_again = input('Awesome, would you like to play again? [y]es/[n]no: ')

    print('Have a good day, Closing the game')

start_game()            # Function call to start the game.
    

