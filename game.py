# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import math
import random

# initialize global variables used in your code
num_range = 100
user_guess = None 
number_choosen = None
guess_remain = 7

# helper function to start and restart the game
def new_game():
    global number_choosen, num_range, guess_remain
    if(num_range == 100):
        print "New game. Range is from 0 to 100"
        guess_remain = 7
    else:
        print "New game. Range is from 0 to 1000"
        guess_remain = 10
    print "Number of remaining guesses is ", guess_remain
    print ""
    number_choosen = random.randrange(0, num_range)
        
# define event handlers for control panel
def range100():
    global num_range
    num_range = 100
    new_game()
          
def range1000():
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global user_guess, number_choosen, guess_remain, num_range
    user_guess = int(guess)
    print "Guess was ", user_guess
    guess_remain -= 1
    print "Number of remaining guesses is ", guess_remain
    if(not(guess_remain)):
        if(user_guess == number_choosen):
            print "Correct!"
        else:
            print "You ran out of guesses. The number was ", number_choosen
        print ""
        new_game();
    else:
        if(user_guess < number_choosen):
                print "Guess Higher!"
                print "" 
        elif(user_guess > number_choosen):
            print "Guess Lower!"
            print ""
        else:
            print "Correct!"
            print ""
            new_game()
            
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200) 

# call new_game and start frame
f.start()
new_game()
# always remember to check your completed program against the grading rubric
