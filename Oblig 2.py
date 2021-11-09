#Gruppe 30 - Håvard, Håkon, Lars, Michael
i = 0
score = 0
FA = []
FQ = []

Q = ["What is the capital of Norway?",
"What is the currency of Norway?",
"What is the largest city in Norway?",
"When is constitution day (the national day) of Norway?",
"What color is the background of the Norwegian flag?",
"How many countries does Norway border?",
"What is the name of the university in Trondheim?",
"How long is the border between Norway and Russia?",
"Where in Norway is Stavanger?",
"From which Norwegian city did the world’s famous composer Edvard Grieg come?"]

CA = [2,3,1,2,1,3,4,2,3,2]

A = [
			["","","",""],
			["","","",""],
			["","","",""],
			["","","",""],
			["","","",""],
			["","","",""],
			["","","",""],
			["","","",""],
			["","","",""],
			["","","",""]
]
								
def main(): 
	global score
	for i in range(10):	
		print(Q[i])
		print(A[i])
	
		condition = True
		while condition:
			answer = input(f'What is the correct answer (1-4?) to question {i+1}: ')
			if answer.isdigit() is False:
				print('Invalid input1')
			elif answer[0] == '0':
				print('Invalid input2')
			elif int(answer) > 0:
				if int(answer) <= 4:
					condition = False 
				else:
					print(f'Invalid input3')
			else:
				print(f'Invalid input4')
		
		if int(answer) == CA[i]: ### list[i]
			score = score + 1
			print("'C'next question")
			
			
			i = i + 1
		else:
			print("'w'next question")
			FQ.append(i)
			FA.append(answer)
			
			i = i + 1
		
			



main()
