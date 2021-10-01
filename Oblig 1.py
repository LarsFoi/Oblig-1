### Enter your bet ### -lars
def bet():
	bet = 0
	bet = input("Enter a how much you want to bet?: ")
	if bet.isdigit():
		if bet >= 1:
			bet = int(bet)
			print(f"{bet} is an accepted amount")
		else :
			print(f"{bet} is not an accepted amount")
			main()			
	else:
		print(f"'{bet}' is an invalid input")
		main()

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


				
				
#def game1():
#	pass		
#		
#
def start():
	bet()

def main():
	guess()
#	
#	while bet > 0:
#		pass
#	
	
guess()
