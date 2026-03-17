"""
File: largest_digit.py
Name: Sidney
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	# t = True
	origin = 0
	n = abs(n)
	return find_largest_digit_helper(n, origin)


def find_largest_digit_helper(n, origin):
	# if t:
	# 	origin = 0
	# 	t = False
	if n/10 == 0:
		return str(origin)
	else:
		digit = int((n / 10 - n // 10) * 10)
		if digit > origin:
			origin = digit
		return find_largest_digit_helper(n/10, origin)

if __name__ == '__main__':
	main()
