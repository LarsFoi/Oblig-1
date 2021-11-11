#Gruppe 30 - Håvard, Håkon, Lars, Michael
score , i = 0 , 0
LOGIN_KEYS = {'username': 'MEK1300', 'password': 'Python'}   
QUESTIONS = ["What is the capital of Norway?","What is the currency of Norway?","What is the largest city in Norway?","When is constitution day (the national day) of Norway?","What color is the background of the Norwegian flag?","How many countries does Norway border?","What is the name of the university in Trondheim?","How long is the border between Norway and Russia?","Where in Norway is Stavanger?","From which Norwegian city did the world’s famous composer Edvard Grieg come?"]
ALTERNATIVES = [["1. Bergen","2. Oslo","3. Stavanger","4. Trondheim"],["1. Euro","2. Pound","3. Krone","4. Deutshe Mark"],["1. Oslo","2. stavanger","3. Bergen","4. Trondheim"],["1. 27th May","2. 17th May","3. 17th April","4. 27th April"],["1. Red","2. White","3. Blue","4. Yellow"],["1. 1","2. 2","3. 3","4. 4"],["1. Uis","2. UiO","3. NMBU","4. NTNU"],["1. 96Km","2. 196Km","3. 296Km","4. 396Km"],["1. North","2. South","3. South-west","4. South-east"],["1. Oslo","2. Bergen","3. Stavanger","4. Tromsø"]]
CORRECT_ANSWERS_TEXT = ["2. Oslo", "3. Krone", "1. Oslo" , "2. 17th May","1. Red","3. 3","4. NTNU","2. 196Km","3. South-west","2. Bergen"]
CORRECT_ANSWERS_NUM = [2,3,1,2,1,3,4,2,3,2]
FALSE_QUESTIONS = []
FALSE_ANSWERS = []
def login_info(): # login (very secure)
	condition = True
	while condition:
		username1 = input('Enter username: ')
		password1 = input('Enter password: ')
		if username1 == LOGIN_KEYS['username'] and password1 == LOGIN_KEYS['password']:
			return True
		else:
			 print('Invalid username and/or password')
def main():
	global score
	print("#——————————————————————————————#\n|The norwegian citizenship test|\n#——————————————————————————————#\n")
	for i in range(10):	# main loop
		print(QUESTIONS[i],"\n")
		for ans in ALTERNATIVES[i]:
			print(ans,"\n")
		condition = True
		while condition: # input-error handeling
			answer = input(f'What is your answer to question {i+1}? (1-4): ')
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
		if i < 9:
			print("Next question,\n\n")	
		if int(answer) == CORRECT_ANSWERS_NUM[i]: # score keeping
			score += 1		
		else: # saves worng answers and questions
			FALSE_QUESTIONS.append(i)
			FALSE_ANSWERS.append(int(answer)-1)					
		i += 1	
	if score == 10: # score board
		print("You got a perfect score!")
	elif score == 9:
		print("This is the question you got wrong:\n")
	elif score == 0:
		print("You got it all wrong. Thats a statistical anomaly!")
	else:
		print(f"You got {score} questions right,\nThese are the {10-score} questions you got wrong:\n")	
	q = 0
	for item in FALSE_QUESTIONS: # loop - wrong answers
		print(f"Question {item+1}:\n"+QUESTIONS[item],"\n\nYou answered:   ", ALTERNATIVES[item][FALSE_ANSWERS[q]],"\nCorrect answer: ", CORRECT_ANSWERS_TEXT[item],"\n")
		q += 1
	print("Thank you for taking the quiz\n")
if login_info():										#Hash to skip login
    print(f"\nLogin sucessfull!\n") # -//-
main()
