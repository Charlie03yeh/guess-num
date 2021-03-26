import random
r = random.randint(1, 100)
while True:
	num = input('請猜數字 ')
	num = int(num)
	if num == r:
		print('你猜對了!')
		break
	else:
		if num > r:
			print('你猜的數字比答案大')
		else:
			print('你猜的數字比答案小')
	