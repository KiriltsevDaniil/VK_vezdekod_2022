import numpy as np

file = open('raw_data.txt', 'r')
passwords = {}


while True:
	number = file.readline()
	password = file.readline()
	skip_line2 = file.readline()
	popularity = file.readline()
	
	if number:
		passwords[number[:-1]] = (password[:-1], int("".join(popularity.split(','))))
	else:
		break
file.close()

flag = True
score = 0
key_opt = ['+', '-', 'q']
helper = "Rules are simple if first password in your opinion is more popular you click + and \
enter, otherwise - and enter, if you get bored click q and enter\n"

print(helper)
while flag:
	equal = True
	while equal:
		pair = np.random.randint(low=1, high=201, size=2)
		if pair[0] != pair[1]:
			equal = False

	pass_1, pass_2 = passwords[str(pair[0])], passwords[str(pair[1])]		
	
	if pass_1[1] >= pass_2[1]:
		answer = '+'
	else:
		answer = '-'

	print(f"Your score is {score}")
	key = input(f"Which is more popular {pass_1[0]} or {pass_2[0]} ?\n")

	if key not in key_opt:
		while key not in key_opt:
			key = input("Oh, poor boy you can input only '+', '-' or 'q'\n")
		
	print(f"{pass_1[0]} has {pass_1[1]} uses \n{pass_2[0]} has {pass_2[1]} uses\n")
	if key == 'q':
		flag = False
		print(f"Your score is {score}")
	else:
		if answer != key:
			print(f"GG You've lost, your score is {score}")
			flag = False
		else:
			score += 1