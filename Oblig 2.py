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

A1 = ["a. Bergen", "b. Oslo", "c. Stavanger", "d. Trondheim"]
A2 = ["a. Euro", 'b. Pound', 'c. Krone', 'd. Deutsche Mark']
A3 = ['a. Oslo', 'b. Stavanger', 'c. Bergen', 'd. Trondheim']


def qna1():
    FA = []
    condition = True
    while condition:
        print(Q[0])
        print(A1[0])
        print(A1[1])
        print(A1[2])
        print(A1[3])
        user_input = input('a, b, c or d: ').lower()
        if user_input not in ('abcd').lower():
            print('Invalid input')
        elif user_input == ('b').lower():
            return 1
        else:
            if user_input == ('a').lower():
                user_input = 'a. Bergen'
            elif user_input == ('c').lower():
                user_input = 'c. Stavanger'
            elif user_input == ('d').lower():
                user_input = 'd. Trondheim'
            FA.append(Q[0])
            FA.append(user_input)
            FA.append(A1[1])
            FA = 'Wrong answer to:',FA[0],'You answered',FA[1],'The right answer is:',FA[2]
            return FA      

def qna2():
    FA = []
    condition = True
    while condition:
        print(Q[1])
        print(A2[0])
        print(A2[1])
        print(A2[2])
        print(A2[3])
        user_input = input('a, b, c or d: ').lower()
        if user_input not in ('abcd').lower():
            print('Invalid input')
        elif user_input == ('c').lower():
            return 1
        else:
            if user_input == ('a').lower():
                user_input = 'a. Euro'
            elif user_input == ('b').lower():
                user_input = 'b. Pound'
            elif user_input == ('d').lower():
                user_input = 'd. Deutsche Mark'
            FA.append(Q[1])
            FA.append(user_input)
            FA.append(A2[2])
            FA = 'Wrong answer to:',FA[0],'You answered',FA[1],'The right answer is:',FA[2]
            return FA

def qna3():
    FA = []
    condition = True
    while condition:
        print(Q[2])
        print(A3[0])
        print(A3[1])
        print(A3[2])
        print(A3[3])
        user_input = input('a, b, c or d: ').lower()
        if user_input not in ('abcd').lower():
            print('Invalid input')
        elif user_input == ('a').lower():
            return 1
        else:
            if user_input == ('b').lower():
                user_input = 'b. Stavanger'
            elif user_input == ('c').lower():
                user_input = 'c. Bergen'
            elif user_input == ('d').lower():
                user_input = 'd. Trondheim'
            FA.append(Q[2])
            FA.append(user_input)
            FA.append(A3[0])
            FA = 'Wrong answer to:',FA[0],'You answered',FA[1],'The right answer is:',FA[2]
            return FA  
        
qna1 = qna1()
print()
qna2 = qna2()
print()
qna3 = qna3()
print()

qna = [qna1, qna2, qna3]

count = 0
for element in qna:
    if element == 1:
        count = count + 1
print(f'You got {count} right question(s)!')

for element in qna:
    if element != 1:
        print (element)
