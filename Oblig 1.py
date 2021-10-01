### script header ###
import sys




### Enter bet-def ### -lars
def bet():
	bet_num = 0
	bet_num = input("Enter a how much you want to bet?: ")
	if bet_num.isdigit():
		bet_num = int(bet_num)
		if bet_num >= 1:
			print(f"{bet} is an accepted amount")
		else :
			print(f"{bet} is not an accepted amount")
			main()
		return bet_num			
	else:
		print(f"'{bet}' is an invalid input")
		main()

### Enter guess-def ### -lars
def guess():
	guess_num = input("What is your guess? (1-50): ")
	if guess_num.isdigit():
		guess_num = int(guess_num)
		if guess_num >= 1 and guess_num <= 50:
			print(f"you entered {guess}")
		else :
			print(f"{guess} is not an accepted guess")
			main()			
	else:
		print(f"'{guess}' is an invalid guess")
		main()
		
### start sequence ### -lars	
def start():
	bet()

### main ###
def main():
	guess()

### game header ###

start()


### main game loop ###
while bet_num > 1:	
	main()
	
	### for loop ###
		# medforsøk 1,2,3 #
	
	
while bet_num <= int(0):
	print("play again?")
	x = input("'y'es or 'n'o")
	if x == "y":
		main()
	else:
		sys.exit()

### game loop end###	
