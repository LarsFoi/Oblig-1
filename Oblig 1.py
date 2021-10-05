# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:26:07 2021

@author: håkon
"""
# Har her satt at man kan kalle seg hva som helst, .,-po9 hvis ønskelig.. 
# ellers tror jeg den fungerer som den skal
# la nå til at initial amount må være større enn 0, men en liten bug der..
# syntes det er litt vanskelig å gjengi hva og hvorfor jeg har gjort som jeg har gjort de ulike stedene, litt vanskelig og rotete men..

from random import randint
# start meny
print('%3s' % '-','%0s' % '', 'Choose any number between 1 and 50.')
print('%3s' % '-','%0s' % '', 'If you guess the number correctly at your 1.st attempt, you will get 10 times the money you bet')
print('%3s' % '-','%0s' % '', 'If you guess the number correctly at your 2.nd attempt, you will get 5 times the money you bet')
print('%3s' % '-','%0s' % '', 'If you guess the number correctly at your 3.rd attempt, you will get 3 times the money you bet')
print('%3s' % '-','%0s' % '', 'If you do not guess the number correctly within three attempts, you will lose your betting amount')

name = input('Please enter your name: ')

# kjører mye while utifra om condition er true eller false, gjør at ting repiteres helt til input er gyldig.

initial_amount = input('Enter your initial amount: ')

# ------ loop for initial amount ---------#
condition = True
while condition:
    if initial_amount.isdigit() is False:               
        condition = True
        while condition:
            print('Invalid input')
            initial_amount = input('Enter your initial amount: ')
            if initial_amount.isdigit() is True:
                condition = False
            else:
                print('',end='')
                
    elif int(initial_amount) <= 0:
            condition = True
            print('Invalid input')
            while condition:
                initial_amount = input('Enter your initial amount: ')
                if initial_amount.isdigit() is True:
                    if int(initial_amount) <= 0:
                        print('Invalid input')
                    else:
                        condition = False
                else:
                    print('Invalid input')
    else:
        condition = False
#---------- loop slutt ------------------#            

def function():
    global initial_amount
    # ---------- loop betting amount -------------#
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
            elif int(betting_amount) == 0:
                print('You got to bet something!')
                break
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
     #--------- loop slutt --------------------#
    
    i = 3 
    #------- loop for num guess (bare første gang) --------#
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
    #---------- loop slutt -----------#
    
    i = 0
    random = randint(1,50)
    winning_amount = 0
    
    #---------- loop for eventuell gevinst og de to neste num guess ------#
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
                print(f'Too high, you got {2-i} attempts left')         # her er (i) = 2-i, slik at (i) går fra 2 til 1 i loopen. (har i=i+1 i slutten av loopen)
                
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
        #------------ loop slutt -----------#
        
    if winning_amount == 0:
        print('You lost your betting amount')
    else:
        print(f'Congratulationt {name}! You won:', winning_amount, '$')
    
    # Utregningen på hvor mye som er igjen på spill-kontoen:
        
    initial_amount = int(initial_amount) - int(betting_amount) + winning_amount
    
    if initial_amount == 0:
        print()
        print(f'Sorry {name}, you lost all your money, thanks for playing!')
    else:
        print('Your initial amount is:', int(initial_amount), '$')
        print('Play again?',end='')
        game = input("'y'es or 'n'o: ")
        if game == 'y':
            function()      # kjører hele funksjonen på nytt hvis 'y'
        elif game == 'n':
            print()
            print(f'Thanks for the game, {name}! You got {initial_amount} $')
        else:
            condition = True
            while condition:
                print('Invalid input')
                game = input("'y'es or 'n'o: ")
                if game == 'y':
                    condition = False
                    function()
                elif game == 'n':
                    print()
                    print(f'Thanks for the game, {name}! You got {initial_amount} $')
                    break
                else:
                    print('',end='')
        
            
function()
        
        

    
    
