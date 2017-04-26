import random

question = []
answer = []
num = 0
cor = 0
wro = 0

def adding():
	global num
	num = 0
	for i in range(3):
		print ('('+str(num)+') Enter question')
		que = input()
		question.append(que)
		
		print ('('+str(num)+') Enter answer')
		ans = input()
		answer.append(ans)
		
		print(question[num] + ' : ' + answer[num])
		
		num = num + 1
		
	print('----------Final list----------')
	for i in range(num):
		print(question[i] +' : '+ answer[i])
		print('------------------------------')
	questionTime()
		
def questionTime():
	global cor
	global wro
	
	cor = 0
	wro = 0
	print('----------Question time----------')
	for i in range(num):
		rand = random.randint(0, num-1)
		print(question[rand])
		guess = input()
		if guess == answer[rand]:
			print('Correct!')
			cor += 1
			continue
		else:
			print('Wrong!')
			wro += 1
			continue
	print('You got ' + str(cor) +' correct and ' + str(wro) + ' wrong.')
	print('Try again?(y/n)')
	again = input()
	if again == 'y':
		questionTime()
		
	else:
		print('Goodbye!')
		quit()
			
def start():
	num = 0
	print('----------Welcome to Flashcard Maker----------')
	print('Type:')
	print('/start - to start making flashcards')
	print('/quit - to quit')
	start = input()
	if start == '/start':
		adding()
	elif start == '/exit':
		print('Goodbye!')
		quit()
	else:
		start()

start()