from tkinter import *


class TrafficLights:
	def __init__(self):
		window = Tk()
		self.var = 1
		window.title("Traffic Lights")

		canvas = Canvas(window, width=100, height=200)
		canvas.pack()
		canvas.create_rectangle(5, 5, 100, 150)
		canvas.create_oval(20, 10, 85, 45, fill=self.setColor(1))
		canvas.create_oval(20, 55, 85, 95, fill=self.setColor(2))
		canvas.create_oval(20, 105, 85, 145, fill=self.setColor(3))

		# todo: fix problem with radio button variable - will not run
		Radiobutton(window, text="red", variable=self.var, value=1).grid(row=1, column=1)
		Radiobutton(window, text="green", variable=self.var, value=2).grid(row=1, column=2)
		Radiobutton(window, text="yellow", variable=self.var, value=3).grid(row=1, column=3)

		window.mainloop()

	# todo: python doesn't have a switch statement, is there a better alternative?
	def setColor(self, val):
		if self.var == val:
			if val == 1:
				return 'red'
			elif val == 2:
				return 'green'
			elif val == 3:
				return 'yellow'
		else:
			return 'white'

TrafficLights()
