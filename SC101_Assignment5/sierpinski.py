"""
File: sierpinski.py
Name: Sidney
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 2                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title='Sierpinski')  # The canvas to draw Sierpinski Triangle


def main():
	"""
	Using Recursion to make a Order 6 sierpinski triangle.
	"""
	window.add(window)
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order:
	:param length:
	:param upper_left_x:
	:param upper_left_y:
	:return:
	"""
	count = 0
	sierpinski_triangle_helper(order, length, upper_left_x, upper_left_y, [], count)


def sierpinski_triangle_helper(order, length, upper_left_x, upper_left_y, order_lst, count):
	count += 1
	if count > order:
		return
	else:
		# for i in range(3**(count-1)):
		# for i in range(count):
		# 	first_x = upper_left_x
		# 	first_y = upper_left_y
		# 	second_x = upper_left_x+length/(2**i)
		# 	second_y = upper_left_y
		# 	third_x = upper_left_x+length/2/(2**i)
		# 	third_y = upper_left_y+length*0.866/(2**i)
		#   basecase放哪邊，如果count == 1 可不可跑
		line1 = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		line2 = GLine(upper_left_x+length, upper_left_y, upper_left_x+length/2, upper_left_y+length*0.866)
		line3 = GLine(upper_left_x + length / 2, upper_left_y + length * 0.866, upper_left_x, upper_left_y)
		window.add(line1)
		window.add(line2)
		window.add(line3)
		#  function會自己往下溝通
		sierpinski_triangle_helper(order, length / 2, upper_left_x, upper_left_y, order_lst, count)  # 左上角
		sierpinski_triangle_helper(order, length / 2, upper_left_x + length/2, upper_left_y, order_lst, count)
		sierpinski_triangle_helper(order, length / 2, upper_left_x + length / 4, upper_left_y + (length * 0.866)/2, order_lst, count)




if __name__ == '__main__':
	main()