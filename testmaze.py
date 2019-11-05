import turtle as t
import time
from makeMazeFile import makeMatrix
from maze import *
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



def fastMazeDrawing(t, matrix, size):
	# faster maze drawing

	# some housekeeping
	t.speed(0)
	t.penup()
	t.shape('square')

	# manual size declaration for now
	t.shapesize(0.5)

	# center this bad boy on the screen

	x = t.pos()[0] - (len(matrix) * size / 2)
	y = t.pos()[1] + (len(matrix[0]) * size / 2)

	# put the turtle at the top left position
	startingPos = [x,y]
	t.setpos(startingPos)

	for arr in matrix:
		# keep track of starting position
		curPos = t.pos()

		for i in range (0, len(arr)):

			if (arr[i] == '#'):
				t.stamp()

			elif (arr[i] == '@'):
				t.fillcolor('green')
				t.stamp()
				t.fillcolor('black')

			elif (arr[i] == 'e'):
				t.fillcolor('gold')
				t.stamp()
				t.fillcolor('black')

			t.forward(size)
			t.penup()

		# move a row down
		t.setpos(curPos[0], curPos[1] - size)


	# return to starting position
	return startingPos

def main():
	t.speed(0)
	matrix = makeMatrix(20, 20)

	homePos = fastMazeDrawing(t.clone(), matrix, 10)
	t.setpos(homePos[0], homePos[1])
	t.showturtle()
	t.pendown()
	t.forward(100)

	print(matrix)
	visited = np.zeros((len(matrix), len(matrix[0])))
	backtrack(t, matrix, homePos, 5, visited)
	time.sleep(5)


if __name__ == '__main__':
	main()
