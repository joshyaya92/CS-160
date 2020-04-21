import sys, turtle as t

studentName = 'Joshua Glenn'

# code that sets up the turtle graphics window
def setup():
	wnWidth = 800
	wnHeight = 800
	
	t.title('CS 160 - Assignment 3 - {studentName}')
	
	t.setup(wnWidth, wnHeight, 0, 0)    # window size, turtle initial position
	
	# set window coordinates of bottom-left corner to 0,0
	t.setworldcoordinates(0, 0, wnWidth, wnHeight)

coords = []


# what to do when the mouse is clicked
def clickFn(x, y):
	t.goto(x, y)
	t.dot(20, 'Purple')
	print([x, y])
	coords.append([x, y])
	print([coords])






def connect():
	t.color('orange')
	t.fillcolor('red')
	t.width(10)
	t.pendown()
	t.goto()
	t.begin_fill()
	t.penup()
	t.end_fill()











  # replace with your own code

# what to do when 'q' is typed on the keyboard
def quitFn():
	sys.exit()

setup()

# set up colors
t.bgcolor('burlywood1')
t.fillcolor('goldenrod')



t.penup()                               # no line when turtle moves
t.hideturtle()                          # no visible turtle

# tell turtle graphics to call clickFn when mouse is clicked
t.onscreenclick(clickFn)

# tell turtle graphics to listen to keyboard, respond to 'q'
t.listen()
t.onkey(quitFn, 'q')
t.onkey(connect, 'd')

t.mainloop()  # keep window open and responsive to mouse, keyboard
