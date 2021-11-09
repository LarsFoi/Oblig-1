#Gruppe 30 - Håvard, Håkon, Lars, Michael
score = 0
i = 1

FA = []
FQ = []

Q = ["What is the capital of Norway?":2,"What is the currency of Norway?":3,"What is the largest city in Norway?":1,"When is constitution day (the national day) of Norway?":2,"What color is the background of the Norwegian flag?":1,"How many countries does Norway border?":3,"What is the name of the university in Trondheim?":4,"How long is the border between Norway and Russia?":2,"Where in Norway is Stavanger?":3,"From which Norwegian city did the world’s famous composer Edvard Grieg come?":2]

A1 = [
			["","","",""]
			["","","",""]
			["","","",""]
			["","","",""]
			["","","",""]
			["","","",""]
			["","","",""]
			["","","",""]
			["","","",""]
			["","","",""]
]
								
def main(): 

for i in Q:
	condition = True
	while condition:
		answer = input(f'What is the correct answer (1-4?) to question {i}: ')
		if answer.isdigit() is False:
			print('Invalid input')
		elif answer[0] == '0':
			print('Invalid input')
		elif int(answer) > 0:
			if int(answer) <= 4:
				condition = False
			else:
				print(f'Invalid input')
	else:
		print(f'Invalid input')
	
	i = i + 1 
		
	if answer == Q.keys(i): ### list[i]
		score = score + 1
		print("next question")
	else:
		print("next question")
		FQ.append(i)
		FA.append(answer)
		
			



main()
