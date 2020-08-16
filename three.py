'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it
'''
from random import shuffle
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list
def player_guess():
    guess = ""
    while guess not in ['0','1','2']:
        guess = input('enter your guess 0,1,2')
    return int(guess)
def check_list(guess,my_list):
    if my_list[guess] == 'O':
        print('your guess is correct')
        print(my_list)
    else:
        print('your guess is wrong')
        print(my_list)

my_list = [' ','O',' ']
mixed_list = shuffle_list(my_list)
guess = player_guess()
check_list(guess,mixed_list)