from tkinter import *

class TrafficLights:
	def __init__(self):
		window = Tk()
		window.title("Traffic Lights")
		var = IntVar()
		var.set(1)

		# todo: draw traffic lights set fill to match oval
		w = Canvas(window, width=100, height=100)

		Radiobutton(window, text="red", variable=var, value=1).grid(row=1, column=1)
		Radiobutton(window, text="green", variable=var, value=2).grid(row=1, column=2)
		Radiobutton(window, text="yellow", variable=var, value=3).grid(row=1, column=4)

		window.mainloop()



TrafficLights()