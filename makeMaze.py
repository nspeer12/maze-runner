import tkinter as tk
import turtle
import time

def makeMaze(matrix, maze):

	# create canvas
	root = tk.Tk()
	canvas = tk.Canvas(master = root, width = 1920, height = 1020)
	canvas.pack()

	# find dimensions
	x = len(matrix)
	y = len(matrix[0])

def main():
	root = tk.Tk()
	canvas = tk.Canvas(master = root, width = 500, height = 500)
	canvas.pack()

	t = turtle.RawTurtle(canvas)
	t.speed(10)
	t.forward(100)

	time.sleep(5)


if __name__ == '__main__':
	main()
