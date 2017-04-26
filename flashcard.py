import random

question = []
answer = []
num = 0
cor = 0
wro = 0

def questionTime():
	cor = 0
	wro = 0
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
		quit()
	
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

print('----------Question time----------')
	
questionTime()