#Gruppe 30 - Håvard, Håkon, Lars, Michael

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

if login_info():
    print('Valid input!')

def q1():
    input_1 = input('What is the capital of Norway?: ')
    if input_1 == 'oslo':
        return 1
rint(q1())


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
