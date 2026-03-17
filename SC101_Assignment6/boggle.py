"""
File: boggle.py
Name:Sidney
----------------------------------------
There are 4 rows (giving 4 alphabets in a row), and
this program help find the word which can be combine
with near alphabets into a words in the dictionary.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	# the base row.
	row_root = 1
	# A switch.
	switch = False
	row_dict = {}
	# for loop to 4 rows.
	for i in range(4):
		n = row_root + i
		row = input(f"{n} row of letters: ")
		for j in range(len(row)):
			if j % 2 == 0 and not row[j].isalpha() or j % 2 == 1 and not row[j].isspace():
				switch = True
		# check the rule of typing
		if switch:
			print('Illegal input.')
			break
		else:
			# save 4 rows in a dict
			row_lst = []  #要小心記得要更新
			ch = row.replace(' ', '')
			row_lst.append(ch.lower())
			row_dict[i] = row_lst
	# for key, value in row_dict.items():  # key=1, 2, 3, 4 value=[ abcd ]
	# 	print(key, value)
	start = time.time()
	####################
	#                  #
	#       TODO:      #
	#                  #d_
	####################
	dict_set = read_dictionary()
	find_permutation(row_dict, dict_set)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	set_dictionary = set()
	with open(FILE, 'r')as f:
		for line in f:
			set_dictionary.add(line.strip())
		return set_dictionary


def find_permutation(row_dict, dict_set):
	ans_lst = []
	# find the start point
	for x in range(len(row_dict[0][0])):
		for y in range(len(row_dict[0][0])):
			# start point
			s = row_dict[x][0][y]
			path = [(x, y)]
			find_permutation_helper(row_dict, dict_set, s, path, ans_lst, (x, y))
	print(f"There are {len(ans_lst)} words in total.")


def find_permutation_helper(row_dict, dict_set, s, path, ans_lst, cur_pos):
	# base case
	if len(s) >= 4:
		if s in dict_set and s not in ans_lst:
			ans_lst.append(s)
			print(f'Found: {s}')
	# notes:: else 會找不到roomy
	cur_x, cur_y = cur_pos
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			next_x = cur_x + i
			next_y = cur_y + j
			# choose
			if 0 <= next_x < len(row_dict[0][0]) and 0 <= next_y < len(row_dict[0][0]):
				if (next_x, next_y) not in path:
					s += row_dict[next_x][0][next_y]
					cur_pos = (next_x, next_y)
					path.append((next_x, next_y))
					# explore
					if has_prefix(s, dict_set):
						find_permutation_helper(row_dict, dict_set, s, path, ans_lst, cur_pos)
					# un choose
					s = s[:-1]
					path.pop()


def has_prefix(sub_s, dict_set):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	word = "".join(sub_s)
	for dict_word in dict_set:
		if dict_word.startswith(word):
			return True
	return False


if __name__ == '__main__':
	main()
