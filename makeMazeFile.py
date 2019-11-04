from random import seed
from random import random
import numpy as np

def makeMazeFile(filename, x, y):
	matrix = []
	hasEntrance = False
	hasExit = False

	for i in range(x):
		subMatrix = []
		for j in range(y):
			if j == 0 or i == 0:
				subMatrix.append('#')
			elif j == y - 1 or i == x -1:
				subMatrix.append('#')
			else:
				rand = random()
				if hasEntrance == False and rand > 0.9:
					subMatrix.append('@')
					hasEntrance = True
				elif hasExit == False and rand < 0.1:
					subMatrix.append('e')
					hasExit = True
				elif rand < 0.3:
					subMatrix.append('#')
				elif rand >= 0.3:
					subMatrix.append('0')

		matrix.append(subMatrix)

	# write maze to file
	file = open(filename, 'w')
	for arr in matrix:
		for j in range(len(arr)):
			file.write(arr[j])
			# add a space except for at the end
			if (j != len(matrix) - 1):
				file.write(' ')
		file.write('\n')
