from makeMazeFile import *
from maze import *
import sys

def makeNMazes(n, dir):
	# starting index is 5 because it is stupid to have a maze any shorter than that
	i = 5
	while(i < n):
		filename = dir + 'maze' + chr(i) + '.txt'
		matrix = makeMatrix(i, i)
		print(matrix)
		# declare visited array here because backtrack function uses it recursively
		visited = np.zeros((n,n))

		# just reuse this function an capture the turtle object
		# will make it easy to modify to show display output in the future
		startingIndex = getStartingIndex(matrix)

		result = backtrack_no_display(matrix, startingIndex, visited)
		print(i, '):',  result)

		if result == True:
			writeMatrixToFile(matrix, filename)
			i += 1
		else:
			continue

	print('successfully created ', n, ' solvable mazes')


def main(*argv):
	n = int(sys.argv[1])
	print(n, ' ', sys.argv[1])

	makeNMazes(n, sys.argv[2])
	return


if __name__ == '__main__':
	main()
