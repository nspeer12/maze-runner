import tkinter as tk
import turtle
import time

def drawCell(t, size, n, char):
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
		for x in range(n):
			for i in range(4):
				t.forward(size)
				t.right(90)
			t.forward(size)
		# set parameters back just incase
		t.end_fill()


def makeMaze(matrix, size):

	# create canvas
	root = tk.Tk()
	canvas = tk.Canvas(master = root, width = 1920, height = 1020)
	canvas.pack()

	# find dimensions
	x = len(matrix)
	y = len(matrix[0])

	# create turtle army
	t = turtle.RawTurtle(canvas)

	tArmy = []
	for i in range(0, x):
		tArmy.append(turtle.RawTurtle(canvas))
		if i > 0:
			tArmy[i].setpos(tArmy[i-1].pos()[0], tArmy[i-1].pos()[1] - size)


	proc = []
	for i in range(len(tArmy)):
		threading.Thread(target = drawCell, args=(tArmy[0], size, 5, '#', )).start()

	for p in proc:
		p.start()

	time.sleep(5)

def main():
	makeMaze([[1,1], [1,1], [1,1], [1,1], [1,1]], 50)


if __name__ == '__main__':
	main()
