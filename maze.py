import turtle as t
import time
import numpy as np


def getMazeFile(filename):
	with open(filename) as f:
		matrix = [l.split() for l in f]

	return matrix

def drawCell(t, size, char):
	if (char == '#'):
		t.fillcolor('grey')
	elif (char == 'e'):
		t.fillcolor('gold')
	elif (char == '@'):
		t.fillcolor('green')
	elif (char == '0'):
		t.fillcolor('white')

	pos = t.pos()

	t.begin_fill()

	# need to optimize drawing maze
	'''
	t.forward(size)
	t.setheading(90)
	t.forward(size)
	t.setheading(180)
	t.forward(size)
	t.setheading(270)
	t.forward(size)
	t.setheading(0)
	'''
	for i in range(4):
		t.forward(size)
		t.right(90)

	# set parameters back just incase
	t.end_fill()



def createMaze(matrix, size):
	# this function draws out a the maze
	# and returns turtle at starting position

	t.speed(0)

	# use this for later
	startingPos = t.pos()
	startingIndex = []

	# traverse cells, right to left, top to bottom
	for i in matrix:
		# track starting position of each row
		pos = t.position()

		# traverse each cell in row
		for x in range(0, len(i)):
			if i[x] == '@':
				startingPos = t.pos()
				startingIndex = [matrix.index(i), x]

			drawCell(t, size, i[x])
			t.forward(size)

		t.setpos(pos)
		t.right(90)
		t.forward(size)
		t.left(90)

	# set to back to starting position
	t.penup()
	t.setpos(startingPos)

	# go to center of the circle
	t.right(90)
	midDist = size/2
	t.forward(midDist)
	t.left(90)
	t.forward(midDist)

	return t, startingIndex

def backtrack(t, matrix, index, size, visited):
	# let's implement this recursively
	i = index[0]
	x = index[1]

	# base case
	if matrix[i][x] == 'e':
		win(t, size)
		return True, [i,x]

	print("i: ", i,  "\tx: ", x)
	visited[i][x] = 1
	print(visited)
	curpos = t.pos()

	print(curpos)
	if valid_move(i - 1, x, matrix, visited) == True:
		t.settiltangle(90)
		print('moving right')
		t.goto(curpos[0], curpos[1] + size)
		t.dot()
		if backtrack(t, matrix, [i - 1, x], size, visited):
			return True

	if valid_move(i + 1, x, matrix, visited) == True:
		print('moving down')
		t.settiltangle(90)
		t.goto(curpos[0], curpos[1] - size)
		t.dot()
		if backtrack(t, matrix, [i + 1, x], size, visited):
			return True

	if valid_move(i, x - 1, matrix, visited) == True:
		print('moving left')
		t.settiltangle(180)
		t.goto(curpos[0] - size, curpos[1])
		t.dot()
		if backtrack(t, matrix, [i, x - 1], size, visited):
			return True


	if valid_move(i, x + 1, matrix, visited) == True:
		print('moving up')
		t.settiltangle(0)
		t.goto(curpos[0] + size, curpos[1])
		t.dot()
		if backtrack(t, matrix, [i, x + 1], size, visited):
			return True

	t.setpos(curpos)
	return False


def valid_move(i, x, matrix, visited):
	if (i < len(matrix) and x < len(matrix[i])):
		if (matrix[i][x] == '0' or matrix[i][x] == 'e'):
			if (visited[i][x] == False):
				return True

	return False

def win(t, size):
	star(t, size)
	return

def star(t, size):
	t.hideturtle()
	colors = ['#2DDFFF', '#F5F474', '#E33CC7', '#FFAA47', '#E53238', '#0064D3', '#F13AB1', '#00B9F1']
	t.speed(200)
	t.backward(size/16)
	t.pendown()

	for color in colors:
		t.fillcolor(color)
		t.begin_fill()
		for i in range(0, 5):
			t.left(360/5)
			t.forward(size/4)
			t.right(360* 2/5)
			t.forward(size/4)

		t.end_fill()
	t.penup()
	return

def main():

	size = 20

	matrix = getMazeFile('maze1.txt')

	y = len(matrix)
	x = len(matrix[0])

	visited = np.zeros((y,x))

	print(visited)


	t, startingIndex = createMaze(matrix, size)
	t.speed(6)
	print(backtrack(t, matrix, startingIndex, size, visited))

	time.sleep(5)


if __name__ == '__main__':
	main()
