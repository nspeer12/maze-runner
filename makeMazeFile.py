from random import seed
from random import random

def makeMazeFile(filename, x, y):
	matrix = []
	hasEntrance = False
	hasExit = False

	for i in range(x):
		subMatrix = []
		for j in range(y):
			if j == 0:
				subMatrix.append('# ')
			elif j == y - 1:
				subMatrix.append('#')
			else:
				rand = random()
				if rand < 0.6:
					subMatrix.append('# ')
				elif rand >= 0.6:
					subMatrix.append('0 ')

		matrix.append(subMatrix)

	print(matrix)
