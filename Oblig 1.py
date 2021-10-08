# Gruppe 30- Håvard, Lars, Michael, Håkon

name = input('Please enter your name: ')
if name == 'hadi':
    name1 = 'king hadi'
    name2 = name1.title()
else:
    name2 = name.title()

print()
print('%61s' % f'Hello {name2}, Welcome to the guessing game! Here are the rules:')
print('-'*63)
print('%3s' % '-','%0s' % '', 'Choose any number between 1 and 50.')
print('%3s' % '-','%0s' % '', 'If you guess the number correctly at your 1.st attempt, you will get 10 times the money you bet')
print('%3s' % '-','%0s' % '', 'If you guess the number correctly at your 2.nd attempt, you will get 5 times the money you bet')
print('%3s' % '-','%0s' % '', 'If you guess the number correctly at your 3.rd attempt, you will get 3 times the money you bet')
print('%3s' % '-','%0s' % '', 'If you do not guess the number correctly within three attempts, you will lose your betting amount')

from random import randint
condition = True
while condition:
    initial_amount = input('Enter your initial amount: ')
    if initial_amount.isdigit() is False:               
        print('Invalid input')
    elif initial_amount[0] == '0':
        print('Invalid input')
    elif int(initial_amount) <= 0:
        print('Invalid input')
    elif int(initial_amount) >= 10000:
        print('You got balls!')
        condition = False
    else:
        condition = False
            

def function(): 
    global initial_amount      
    condition = True
    while condition:
        betting_amount = input('Enter a betting amount: ')
        if betting_amount.isdigit() is True:
            if betting_amount[0] == '0':
                print('Invalid input')
            elif int(betting_amount) > 0 and int(betting_amount) <= int(initial_amount):
                condition = False
            else:
                if int(betting_amount) == 0:
                    print('You gotta bet something!')
                elif int(betting_amount) < 0:
                    print('You cant bet negative')
                else:
                    print(f'You cant bet more than your initial amount ({initial_amount} $)')
        else:
            print('Invalid input')

    i = 0
    random = randint(1,50)
    winning_amount = 0
    for i in range(3):
        condition = True
        while condition:
            num_guess = input('Enter a number between 1 and 50: ')
            if num_guess.isdigit() is False:
                print(f'Invalid input, you got {3-i} attempts left')
                num_guess = input('Enter a number between 1 and 50: ')
                if num_guess.isdigit() is True:
                    if int(num_guess) <= 50 and int(num_guess) > 0:
                        condition = False
                    else:
                        print(f'Invalid input, you got {3-i} attempts left')
                else:
                    print(f'Invalid input, you got {3-i} attempts left')
            elif num_guess[0] == '0':
                print('Invalid input')
            elif int(num_guess) > 0:
                if int(num_guess) <= 50:
                    condition = False
                else:
                    print(f'Invalid input, you got {3-i} attempts left')
            else:
                print(f'Invalid input, you got {3-i} attempts left')
        
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
                
        i = i + 1
        
    if winning_amount == 0:
        print(f'You lost your betting amount, correct number was {random}')
    else:
        print(f'Congratulationt {name2}! You won:', winning_amount, '$')
    
    # Utregningen på hvor mye som er igjen på spill-kontoen:
        
    initial_amount = int(initial_amount) - int(betting_amount) + winning_amount
    
    if initial_amount == 0:
        print()
        print(f'Sorry {name2}, you lost all your money, thanks for playing!')
    else:
        print('Your initial amount is:', int(initial_amount), '$')
        print('Play again?',end='')
        game = input("'y'es or 'n'o: ")
        if game == 'y':
            function()      # kjører hele funksjonen på nytt hvis 'y'
        elif game == 'n':
            print()
            print(f'Thanks for the game, {name2}! You got {initial_amount} $')
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
                    print(f'Thanks for the game, {name2}! You got {initial_amount} $')
                    break
                else:
                    print('',end='')
        
            
function()
        
        

    
    
