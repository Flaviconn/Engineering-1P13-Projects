"""
Thomas Brittain
brittt2@mcmaster.ca
400650099

A party game with 3 different games, pig, slot machine and look away!
The program lets the player play any of the games, accumulating points, until they decide to stop.
"""

import random
import time

def print_signature():
    '''
    This feels extra to put, but the documentation standards told me to...
    This function prints my information!
    '''
    print('Thomas Brittain\n400650099 Engineering 1\nENG 1P13: Integrated Cornerstone Design Projects in Engineering\nDr. Sam Scott\nFall 2025')

def look_away(first_move,second_move,third_move):
    '''
    This function takes 3 inputs as moves for 3 rounds of 'look away' and compares them with 2 bots.
    The function returns the total number of points gained from all 3 rounds!
    '''
    def direction_change(num):
        '''
        This just converts the integer inputs into their corresponding directions as strings.
        '''
        if num=='1':
            return('up')
        elif num=='2':
            return('down')
        elif num=='3':
            return('left')
        elif num=='4':
            return('right')
        else:
            print('Your input is not correct... Defaulting to up')
            return('up')
    
    def lookaway_check(b1,b2,p1):
        '''
        This checks the result of one round, prints the corresponding text output, and returns the number of points for the 1 round.
        '''
        if p1==b1 or p1==b2:
            print(f"Round 1: Bot 1 chose {b1}, Bot 2 chose {b2}, and you chose {p1}. You lose!")
            return(0)
        else:
            print(f"Round 1: Bot 1 chose {b1}, Bot 2 chose {b2}, and you chose {p1}. You Win!")
            return(10)
    
    #This is my overall score variable which I increment after every round and return at the end of the function.
    score=0

    #Using my above function to set all my moves to their corresponding strings.
    first_move=direction_change(first_move)
    second_move=direction_change(second_move)
    third_move=direction_change(third_move)

    #Runs the 3 individual rounds with 2 random bot inputs each time. I put the sleep so it doesn't just blast the user with information and go back to the homepage.
    for i in range(3):
        bot_1=direction_change(str(random.randint(1,4)))
        bot_2=direction_change(str(random.randint(1,4)))
        time.sleep(1)

        if i==0:
            score+=lookaway_check(bot_1,bot_2,first_move)

        elif i==1:
            score+=lookaway_check(bot_1,bot_2,second_move)

        elif i==2:
            score+=lookaway_check(bot_1,bot_2,third_move)

    return(score)

def slot_machine(bet):
    '''
    My slot machine function! This generates 3 random symbols and checks them to see if the user won! (2 equal or 3 equal)
    The function returns the number of points won based on the result of the game.
    This function doesn't return negative points for a loss (no matches). The main game room subtracts the points after the bet.
    '''
    def rand_symbol():
        '''
        Just a helper function to create random symbols without lists.
        This doesn't take any parameters, it just returns the random symbol.
        '''
        n=random.randint(1,4)
        if n==1:
            return('@')
        elif n==2:
            return('#')
        elif n==3:
            return('$')
        else:
            return('%')
    
    #generating the results of the slot machine
    s1=rand_symbol()
    s2=rand_symbol()
    s3=rand_symbol()

    #Printing the results on the same line with a little bit of suspense ..... !
    print(s1, end='  ')
    time.sleep(1)
    print(s2, end='  ')
    time.sleep(2)
    print(s3)

    #The main logic for checking the result and returning the correct number of points.
    if s1==s2==s3:
        return(bet*5)
    elif s1==s2 or s1==s3 or s2==s3:
        return(bet*2)
    else:
        return(0)

def pig_dice(threshold):
    '''
    This takes the threshold as given by the user and rolls 2 dice until either there is a 1, two ones, or the value is greater than the threshold!
    The program returns 
    '''
    #This value is incremented each time the dice are rolled and is returned if there isn't a loss or catastrophic loss.
    score=0

    #This string has the threshold and is updated after every roll. It is printed along with the result of the game for each cooresponding return statement.
    output=str('Threshold:'+str(threshold)+' Rolls:')

    #Runs until the game is won, or until a return statement at a loss or catastrophic loss.
    while score<=threshold:
        #My two dice rolls
        d1=random.randint(1,6)
        d2=random.randint(1,6)
        
        #Updating score and output string as stated above.
        score+=(d1+d2)
        output=output+f'({d1}, {d2}) '
        
    #Logic for the game, returning the correct values (-1,0,score) according to the assignment rules, along with an output string.
        if d1==1 and d2==1:
            print(output,'Catastrophic loss!', sep='')
            return(-1)
        elif d1==1 or d2==1:
            print(output, 'Loss', sep='')
            return(0)
    print(output, 'Win!', sep='')
    return(score)

def games_room(name, score=int(0)):
    '''
    My main game room!
    This takes the player's name, then loops through the selection menu until the player presses 4 to exit!
    This runs all the above game functions depending on the player's selection,
    '''

    play=True
    
    while play:
        #This prints a nice menu string, asks for the user's input and stores it!
        choice=input(('Welcome to MacParty, '+name+'!\nYou have '+str(score)+' points!\nEnter 1 to play Lookaway\nEnter 2 to play Slot Machine\nEnter 3 to play Pig\nEnter 4 to quit.\n'))
        
        #Prompts the user for the direction for 3 rounds and plays look away!
        if choice=='1':
            score+=look_away(input('Enter your direction for each round!\n1 is up, 2 is down, 3 is left and 4 is right.\n'),input(''),input(''))
        
        #Asks for a bet and runs the slot machine function
        elif choice=='2':
            bet=int(input('Enter your number bet for the slots!\n'))
            if bet>score:
                print("You don't have enough points for that!\nReturning to the menu.")
            elif bet<0:
                print("You aren't a kind person! Reconsider.\nReturning to the menu.")
            else:
                score-=bet
                score+=(slot_machine(bet))

        #Asks for the user's threshold and runs the pig game with it.
        elif choice=='3':
            threshold=int(input('Enter your number threshold for the pig game!\n'))
            if threshold<0:
                print("You really don't have to do this to me...\nReturning to menu.")
            else:
                pig_result=pig_dice(threshold)
                if pig_result==-1:
                    score=0
                else:
                    score+=pig_result

        #Sets my play to false to stop the loop!
        elif choice=='4':
            print(score)
            play=False
        
        #Just in case the user errors. I tried to error catch without using try statements. The only non-fool proof places are the inputs for the pig game and the slot as I can't int check.
        else:
            print('Unknown input... Please try again!')
    
    #Makes it so my game doesn't just exit instantly if it's not being run in an IDE for example.
    input('Thank you for playing!\n Press enter to exit.')

#Runs my game!
print_signature()
games_room(input('Welcome to MacParty!\nEnter your name to begin:\n'))