# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:26:07 2021

@author: haako
"""

# Har her satt at man kan kalle seg hva som helst, .,-po9 hvis ønskelig.. 
# ellers tror jeg den fungerer som den skal

from random import randint

print('%3s' % '-','%0s' % '', 'Choose any number between 1 and 50.')
print('%3s' % '-','%0s' % '', 'If you guess the number correctly at your 1.st attempt, you will get 10 times the money you bet')
print('%3s' % '-','%0s' % '', 'If you guess the number correctly at your 2.nd attempt, you will get 5 times the money you bet')
print('%3s' % '-','%0s' % '', 'If you guess the number correctly at your 3.rd attempt, you will get 3 times the money you bet')
print('%3s' % '-','%0s' % '', 'If you do not guess the number correctly within three attempts, you will lose your betting amount')

name = input('Please enter your name: ')

initial_amount = input('Enter your initial amount: ')
if initial_amount.isdigit() is False:
    condition = True
    while condition:
        print('Invalid input')
        initial_amount = input('Enter your initial amount: ')
        if initial_amount.isdigit() is True:
            condition = False

    

def function():
    global initial_amount
    condition = True
    while condition:
        betting_amount = input('Enter a betting amount: ')
        if betting_amount.isdigit() is False:
            condition = True
            while condition:
                print('Invalid input')
                betting_amount = input('Enter your betting amount: ')
                if betting_amount.isdigit() is True:
                    condition = False
        else:
            condition = False
            
        condition = True
        while condition:
            if int(betting_amount) > 0:
                if int(betting_amount) <= int(initial_amount):
                    condition = False
                else:
                    print(f'You can not bet more than your initial amount ({initial_amount} $)')
                    betting_amount = input('Enter a betting amount: ')
                    if betting_amount.isdigit() is False:
                        condition = True
                        while condition:
                            print('Invalid input')
                            betting_amount = input('Enter your betting amount: ')
                            if betting_amount.isdigit() is True:
                                condition = False
            else:
                print('You can not bet a negative number')
                betting_amount = input('Enter a betting amount: ')
                if betting_amount.isdigit() is False:
                    condition = True
                    while condition:
                        print('Invalid input')
                        betting_amount = input('Enter your betting amount: ')
                        if betting_amount.isdigit() is True:
                            condition = False
                
    i = 3            
    condition = True
    while condition:
        num_guess = input('Enter a number between 1 and 50: ')
        if num_guess.isdigit() is False:
            print(f'Invalid input, you got {i} attempts left')
            num_guess = input('Enter a number between 1 and 50: ')
            if num_guess.isdigit() is True:
                condition = False
            else:
                print(f'Invalid input, you got {i} attempts left')
        else:
            if int(num_guess) > 0:
                if int(num_guess) <= 50:
                    condition = False
                else:
                    print(f'Invalid input, you got {i} attempts left')
            else:
                print(f'Invalid input, you got {i} attempts left')
    
    i = 0
    random = randint(1,50)
    winning_amount = 0
    while i < 2:
        if i == 0 and random == int(num_guess):
            winning_amount = int(betting_amount) * 10
            break
        elif i == 1 and random == int(num_guess):
            winning_amount = int(betting_amount) * 5
            break
        elif i == 2 and random == int(num_guess):
            winning_amount = int(betting_amount) * 3
            break
        elif i == 2 and random != int(num_guess):
            winning_amount = int(betting_amount) * 0
            
        else:
            if int(num_guess) < random:
                print(f'Too low, you got {2-i} attempts left')
            else:
                print(f'Too high, you got {2-i} attempts left')
                
        condition = True
        while condition:
            num_guess = input('Enter a number between 1 and 50: ')
            if num_guess.isdigit() is False:
                print(f'Invalid input, you got {2-i} attempts left')
                num_guess = input('Enter a number between 1 and 50: ')
                if num_guess.isdigit() is True:
                    condition = False
                else:
                    print(f'Invalid input, you got {2-i} attempts left')
            elif int(num_guess) > 0:
                if int(num_guess) <= 50:
                    condition = False
                else:
                    print(f'Invalid input, you got {2-i} attempts left')
            else:
                print(f'Invalid input, you got {2-i} attempts left')
        
        i = i + 1
        
    if winning_amount == 0:
        print('You lost your betting amount')
    else:
        print(f'Congratulationt {name}! You won:', winning_amount, '$')
    
    initial_amount = int(initial_amount) - int(betting_amount) + winning_amount
    
    if initial_amount == 0:
        print()
        print(f'Sorry {name}, you lost all your money, thanks for playing!')
        
    
    
    else:
        print('Your initial amount is:', int(initial_amount), '$')
        print('Play again?',end='')
        game = input("'y'es or 'n'o: ")
        if game == 'y':
            function()
        elif game == 'n':
            print()
            print(f'Thanks for the game, {name}! You got {initial_amount} $')
        else:
            while game != 'y' or game != 'n':
                print('Invalid input')
                game = input("'y'es or 'n'o: ")
                if game == 'y':
                    function()
                elif game == 'n':
                    print()
                    print(f'Thanks for the game, {name}! You got {initial_amount} $')
                    break
        
            
function()
        
        

    
    
