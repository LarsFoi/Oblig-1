### Enter your bet ### -lars
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
		print("You must input the amount you want to bet")
		main()
		
#def game1():
#	pass		
#		
#
def main():
	bet()
#	
#	while bet > 0:
#		pass
#	
	
main()
