"""
File Name: main.py
Developer: Jonathan Martinez
Date last modified: September 29, 2017
Description: Analyzing dice rolls is a common example in understanding probability and statistics.
             The following program calculates the number of times the sum of two randomnly rolled dices. 
             A histogram, in which the total number of times the dice rolls equals each possible
             value, is displayed by printing a character, such as *, that number of times.
email address: jonathanmartineztek@gmail.com
"""
import random

num_twos = ''
num_threes = ''
num_fours = ''
num_fives = ''
num_sixes = ''
num_sevens = ''
num_eights = ''
num_nines = ''
num_tens = ''
num_elevens = ''
num_twelves = ''

num_rolls = int(input('Enter number of rolls: '))
if num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

        #Count number of ones,twos,..., and twelves
        if roll_total == 2:
            num_twos += '* '
        if roll_total == 3:
            num_threes += '* '
        if roll_total == 4:
            num_fours += '* '
        if roll_total == 5:
            num_fives += '* '
        if roll_total == 6:
            num_sixes += '* '
        if roll_total == 7:
            num_sevens += '* '
        if roll_total == 8:
            num_eights += '* '
        if roll_total == 9:
            num_nines += '* '
        if roll_total == 10:
            num_tens += '* '
        if roll_total == 11:
           num_elevens += '* '
        if roll_total == 12:
            num_twelves += '* '

    print('\n-----------------------------')
    print(' Dice roll Histogram:\n')
    print(' 2s: ', num_twos)
    print(' 3s: ', num_threes)
    print(' 4s: ', num_fours)
    print(' 5s: ', num_fives)
    print(' 6s: ', num_sixes)
    print(' 7s: ', num_sevens)
    print(' 8s: ', num_eights)
    print(' 9s: ', num_nines)
    print(' 10s:', num_tens)
    print(' 11s:', num_elevens)
    print(' 12s:', num_twelves)
    print('-----------------------------')

else:
    print('Invalid number of rolls. Try again.')
