### script header ###
import sys
from random import randrange
bet_num = 0
guess_num = 0
random_num = 0

### Enter bet-def ### -lars
def bet():
	bet_num = input("Enter a how much you want to bet?: ")
	if bet_num.isdigit():
		bet_num = int(bet_num)
		if bet_num >= 1:
			print(f"{bet_num} is an accepted amount")
			return int(bet_num)
		else:
			print(f"{bet_num} is not an accepted amount")
	else:
		print(f"'{bet_num}' is an invalid input")

### Enter guess-def ### -lars
def guess():
	guess_num = input("What is your guess? (1-50): ")
	if guess_num.isdigit():
		guess_num = int(guess_num)
		if guess_num >= 1 and guess_num <= 50:
			print(f"you entered {guess_num}")
			return int(guess_num)
		else:
			print(f"'{guess_num}' is not an accepted guess")
	else:
		print(f"'{guess_num}' is an invalid guess")

### start sequence ### -lars	
def start():
	bet()

### main ###
def main():
	guess()
	random_num = int(randrange(1,50))
	print(f"the number is {random_num}")
	if int(guess_num) == int(random_num):
		bet_num = bet_num * 10
		print(f"your score is {bet_num}")
		return int(bet_num)
	else:
		print("too bad, you have 2 etempts left")
	guess()
	if guess_num == random_num:
		bet_num = bet_num * 5
		print(f"your score is {bet_num}")
		return int(bet_num)
	else:
		print("too bad, you have 1 etempt left")
	guess()
	if guess_num == random_num:
		bet_num = bet_num * 3
		print(f"your score is {bet_num}")
		return int(bet_num)
	else:
		print("you loose")
		bet_num = 0

### game header ###

start()

### main game loop ###
while bet_num > 0:	
	main()
	
	
while bet_num <= 0:
	print("play again?")
	x = input("'y'es or 'n'o: ")
	if x == "y":
		start()
		main()
	else:
		sys.exit()

### game loop end###	
