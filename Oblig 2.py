#Gruppe 30 - Håvard, Håkon, Lars, Michael
import time
score = 0
i = 0
FQ = []
FA = []
login_keys = {'username': 'MEK1300', 'password': 'Python'}
def login_info():
    condition = True
    while condition:
        username1 = input('Enter the username: ')
        password1 = input('Enter the password: ')
        if username1 == login_keys['username'] and password1 == login_keys['password']:
            return True
        else:
            print('Invalid username and/or password')
            
Q = ["What is the capital of Norway?","What is the currency of Norway?","What is the largest city in Norway?","When is constitution day (the national day) of Norway?","What color is the background of the Norwegian flag?","How many countries does Norway border?","What is the name of the university in Trondheim?","How long is the border between Norway and Russia?","Where in Norway is Stavanger?","From which Norwegian city did the world’s famous composer Edvard Grieg come?"]
CA = [2,3,1,2,1,3,4,2,3,2]
CA1 = ["2. Oslo", "3. Krone", "1. Oslo" , "2. 17th May","1. Red","3. 3","4. NTNU","2. 196Km","3. South-west","2. Bergen"]
A = [["1. Bergen","2. Oslo","3. Stavanger","4. Trondheim"],["1. Euro","2. Pound","3. Krone","4. Deutshe Mark"],["1. Oslo","2. stavanger","3. Bergen","4. Trondheim"],["1. 27th May","2. 17th May","3. 17th April","4. 27th April"],["1. Red","2. White","3. Blue","4. Yellow"],["1. 1","2. 2","3. 3","4. 4"],["1. Uis","2. UiO","3. NMBU","4. NTNU"],["1. 96Km","2. 196Km","3. 296Km","4. 396Km"],["1. North","2. South","3. South-west","4. South-east"],["1. Oslo","2. Bergen","3. Stavanger","4. Tromsø"]]	
					
def main(): 
	global score
	global fa
	for i in range(10):	
		print(Q[i],"\n")
		for ans in A[i]:
			print(ans,"\n")
		condition = True
		while condition:
			answer = input(f'What is the correct answer (1-4) to question {i+1}: ')
			if answer.isdigit() is False:
				print('Invalid input')
			elif answer[0] == '0':
				print('Invalid input')
			elif int(answer) > 0:
				if int(answer) <= 4:
					condition = False
					print()
				else:
					print(f'Invalid input')
			else:
				print(f'Invalid input')	
					
		if int(answer) == CA[i]: ### list[i]
			score = score + 1		
			i = i + 1
		else:
			FQ.append(i)
			FA.append(int(answer)-1)	
				
			i = i + 1	
	
	if score == 10:
		print("You got a perfect score!")
	elif score == 9:
		print("This is the question you got wrong:\n")
	elif score == 0:
		print("Your score is 0. Thats a statistical anomaly!")
	else:
		print(f"You got {score} questions right\n")
		print("These are the questions you got wrong:\n")
		
	i = 0	
	
	for item in FQ:
		print(f"Question {item+1}:")
		print(Q[item],"\n")
		print("You answered:   ", A[item][FA[i]])
		print("Correct answer: ", CA1[item],"\n")
		i = i + 1
		time.sleep(1)

if login_info():
    print(f"\nLogin sucessfull!\n")

main()
