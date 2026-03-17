"""
File: coin_flip_runs.py
Name: Sidney
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	TODO: coin flip runs
	"""
	print("Let's flip a coin! ")   # title
	num_runs = int(input('Number of runs: '))    # users can give how many times of runs
	num = 0
	is_in_a_row = False
	a_ch = random_alphabet()
	ch = a_ch
	while True:
		b_ch = random_alphabet()
		if num != num_runs:
			if a_ch == b_ch:
				if not is_in_a_row:
					num += 1
					is_in_a_row = True
			else:
				is_in_a_row = False
			a_ch = b_ch
			ch += a_ch
		else:
			print(str(ch))
			break


def random_alphabet():
	alp = r.choice(range(2))
	if alp == 0:
		return'H'
	if alp == 1:
		return'T'





# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
