### script header ###
import sys




### Enter bet ### -lars
def bet():
	bet = 0
	bet = input("Enter a how much you want to bet?: ")
	if bet.isdigit():
		bet = int(bet)
		if bet >= 1:
			print(f"{bet} is an accepted amount")
		else :
			print(f"{bet} is not an accepted amount")
			main()			
	else:
		print(f"'{bet}' is an invalid input")
		main()
	return int(bet)

### start sequence ### -lars	
def start():
	bet()

### Enter guess ### -lars
def guess():
	guess = input("What is your guess? (1-50): ")
	if guess.isdigit():
		guess = int(guess)
		if guess >= 1 and guess <= 50:
			print(f"you entered {guess}")
		else :
			print(f"{guess} is not an accepted guess")
			main()			
	else:
		print(f"'{guess}' is an invalid guess")
		main()

### main ###
def main():
	guess()

### game header ###

start()


### main game loop ###
while bet > 0:	
	main()
	
	
while bet <= 0:
	print("play again?")
	x = input("'y'es or 'n'o")
	if x == "y":
		main()
	else:
		sys.exit()

### game loop end###	
