import turtle as t
import time
import sys
from random import random
import numpy as np

class MazeRunner:
	t = None
	size = 0
	n = 0
	matrix = None
	startingPos = None
	startingIndex = [0,0]

	def __init__(self, size, n):
		self.size = size
		self.n = n


	def drawMaze(self):
		# faster maze drawing
		t.speed(20)
		# some housekeeping
		t.penup()
		t.shape('square')

		# manual size declaration for now
		t.shapesize(0.5)

		# center this bad boy on the screen
		x = t.pos()[0] - (self.n * self.size / 2)
		y = t.pos()[1] + (self.n * self.size / 2)

		# put the turtle at the top left position
		startingPos = [x,y]
		t.setpos(startingPos)

		for arr in self.matrix:
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

				t.forward(self.size)
				t.penup()

			# move a row down
			t.setpos(curPos[0], curPos[1] - self.size)


		# return to starting position
		t.setpos(startingPos[0], startingPos[1])
		self.startingPos = startingPos


	def makeRandomMatrix(self):
		matrix = []
		hasEntrance = False
		hasExit = False

		for i in range(self.n):
			subMatrix = []
			for j in range(self.n):
				if j == 0 or i == 0:
					subMatrix.append('#')
				elif j == self.n - 1 or i == self.n -1:
					subMatrix.append('#')
				else:
					rand = random()
					if hasEntrance == False and rand > 0.95:
						subMatrix.append('@')
						# set starting position
						self.startingIndex = [i, j]
						hasEntrance = True
					elif hasExit == False and rand < 0.05:
						subMatrix.append('e')
						hasExit = True
					elif rand < 0.3:
						subMatrix.append('#')
					elif rand >= 0.3:
						subMatrix.append('0')

			matrix.append(subMatrix)

		self.matrix = matrix
		return

	def backtrack_no_display(self, index, visited):

		# let's implement this recursively
		i = index[0]
		x = index[1]

		# base case
		if self.matrix[i][x] == 'e':
			return True, [i,x]

		print("i: ", i,  "\tx: ", x)
		visited[i][x] = 1

		if valid_move(i - 1, x, self.matrix, visited) == True:
			print('right')
			if self.backtrack_no_display([i - 1, x], visited):
				return True

		if valid_move(i + 1, x, self.matrix, visited) == True:
			print('down')
			if self.backtrack_no_display([i + 1, x], visited):
				return True

		if valid_move(i, x - 1, self.matrix, visited) == True:
			print('left')
			if self.backtrack_no_display([i, x - 1], visited):
				return True


		if valid_move(i, x + 1, self.matrix, visited) == True:
			print('up')
			if self.backtrack_no_display([i, x + 1], visited):
				return True

		return False

	def backtrack(self):
		t.speed(5)
		t.setpos(self.startingIndex[0], self.startingIndex[0])
		self.backtrack_recursive(t, self.startingIndex, np.zeros((self.n, self.n)))

	def backtrack_recursive(self, t, index, visited):

		# let's implement this recursively
		i = int(index[0])
		x = int(index[1])

		# base case
		if self.matrix[i][x] == 'e':
			return True, [i,x]

		print("i: ", i,  "\tx: ", x)
		visited[i][x] = 1

		curpos = t.pos()

		if valid_move(i - 1, x, self.matrix, visited) == True:
			print('right')
			# move turtle
			self.t.settiltangle(90)
			self.t.goto(curpos[0], curpos[1] + size)
			t.dot()

			if self.backtrack_recursive([i - 1, x], t, visited):
				return True

		if valid_move(i + 1, x, self.matrix, visited) == True:
			print('down')

			self.t.settiltangle(270)
			self.t.goto(curpos[0], curpos[1] - size)
			self.t.dot()

			if self.backtrack_recursive([i + 1, x], t, visited):
				return True

		if valid_move(i, x - 1, self.matrix, visited) == True:
			print('left')
			self.t.settiltangle(180)
			self.t.goto(curpos[0] - size, curpos[1])
			self.t.dot()
			if self.backtrack_recursive([i, x - 1], t, visited):
				return True


		if valid_move(i, x + 1, self.matrix, visited) == True:
			print('up')
			self.t.settiltangle(0)
			self.t.goto(curpos[0] + size, curpos[1])
			self.t.dot()
			if self.backtrack_recursive([i, x + 1], t, visited):
				return True

		return False

def valid_move(i, x, matrix, visited):
	if (i < len(matrix) and x < len(matrix[i])):
		if (matrix[i][x] == '0' or matrix[i][x] == 'e'):
			if (visited[i][x] == False):
				return True

	return False

def main():
	n = 10
	runner = MazeRunner(10, n)

	# create a maze that is actually solveable

	solveable = False
	while(solveable != True):
		runner.makeRandomMatrix()
		solveable = runner.backtrack_no_display(runner.startingPos, np.zeros((n,n)))


	runner.drawMaze()
	runner.backtrack()
	time.sleep(1)


if __name__ == '__main__':
	main()
