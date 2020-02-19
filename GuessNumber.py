import random
counts = 3
while counts > 0:
	print("please input one number:/n")
	temp = input()
	guess = int(temp)
	anwser = random.randint(0,10)
	if guess == anwser:
		print('you are right')
		break
	elif guess > anwser:
		print('your guess is bigger')
	else:
		print('your guess is more smaller')
	counts = counts -1
	print('game over')
