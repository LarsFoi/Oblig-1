########---to do---################################
# 1. legg til balance i start sequence
# 2. 
# 3. 
# 4. 
###################################################

### script header ###
import sys
from random import randrange
bet_num = 0
guess_num = 0
random_num = 0
balance = 0

### start sequence --- ###
def start():
	bet()

### Enter bet-def ###
def bet():
	global bet_num
	bet_num = input("Enter a how much you want to bet?: ")
	if bet_num.isdigit():
		bet_num = int(bet_num)
		if bet_num >= 1:
			print(f"{bet_num} is an accepted amount")
		else:
			print(f"{bet_num} is not an accepted amount")
	else:
		print(f"'{bet_num}' is an invalid input")
	return int(bet_num)

### Enter guess-def ###
def guess():
	global guess_num
	guess_num = input("What is your guess? (1-50): ")
	if guess_num.isdigit():
		guess_num = int(guess_num)
		if guess_num >= 1 and guess_num <= 50:
			print(f"you entered {guess_num}")
		else:
			print(f"'{guess_num}' is not an accepted guess")
	else:
		print(f"'{guess_num}' is an invalid guess")
	return int(guess_num)

### main ###
def main():
	global bet_num
	global guess_num
	
	## guess 1 ##
	guess()
	random_num = int(randrange(1,50))
	print(f"###the number is {random_num}###") ### debugging - bare sånn at vi kan se hva tallet er ###
	if int(guess_num) == int(random_num):
		bet_num = bet_num * 10
		print(f"your score is {bet_num}")
		return int(bet_num)
	else:
		if guess_num > random_num:
			print("too hight, you have 2 etempts left")
		else:
			print("to low; you have 2 etempts left")
	
	## guess 2 ##
	guess()
	if guess_num == random_num:
		bet_num = bet_num * 5
		print(f"your score is {bet_num}")
		return int(bet_num)
	else:
		if guess_num > random_num:
			print("too hight, you have 2 etempts left")
		else:
			print("to low; you have 2 etempts left")
			
	## guess 3 ##
	guess()
	if guess_num == random_num:
		bet_num = bet_num * 3
		print(f"your score is {bet_num}")
		return int(bet_num)
	else:
		print("you loose")
		bet_num = 0
		return int(bet_num)

### game header ###

start()
main()

### game loop ###
while bet_num > 0:	
	print(f"You won! play again? Your score is {bet_num}")
	x = input("'y'es or 'n'o: ")
	if x == "y":
		main()
	else:
		sys.exit()
	
while bet_num <= 0:
	print("You lose, play again?")
	x = input("'y'es or 'n'o: ")
	if x == "y":
		start()
		main()
	else:
		sys.exit()

### game loop end###	
