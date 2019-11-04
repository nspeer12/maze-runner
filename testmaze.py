import turtle as t
import time
from makeMazeFile import makeMatrix

def drawMaze(size, matrix):
	t.speed(0)
	t.hideturtle()

	for arr in matrix:
		pos = t.pos()
		drawRow(t, arr, size)
		t.penup()
		t.setpos(pos[0], pos[1] - size)
		t.pendown()


def drawRow(t, arr, size):

	for i in range(len(arr)):
		# assign color
		if (arr[i] == '#'):
			t.fillcolor('grey')
		elif (arr[i] == 'e'):
			t.fillcolor('gold')
		elif (arr[i] == '@'):
			t.fillcolor('green')
		elif (arr[i] == '0'):
			t.fillcolor('white')

		t.begin_fill()
		degree = 0
		for j in range(4):
			print(degree)
			# case to use so we can set the degree back to 0 instead of 360
			if j != 3:
				degree = degree + 90
				t.setheading(degree)
				t.forward(size)
			elif i != len(arr) - 1:
				degree = 0
				t.setheading(degree)
				t.forward(size * 2)
			else:
				break

		t.end_fill()


def main():
	matrix = makeMatrix(100, 100)
	print(matrix)
	drawMaze(10, matrix)


if __name__ == '__main__':
	main()
