for i in range(0,101):
	if i % 7 == 0:
		continue
	elif i % 10 == 7:
		continue
	elif i // 10 == 7:
		continue
	else:
		print('{}'.format(i))

