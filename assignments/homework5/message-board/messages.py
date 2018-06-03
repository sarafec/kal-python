from tkinter import *

class MessageBoard:
	def __init__(self):
		window = Tk()
		self.messageVal = 1
		window.title("Message Board")
		Label(window, text="Message:").grid(row=1, column=1, sticky=W)

		self.messageVar = StringVar()
		Label(window, textvariable=self.messageVar, justify=RIGHT).grid(row=1, column=2)
		self.messageVar.set("Programming is fun")

		# sets click event
		window.bind("<Button-1>", self.setMessage)
		window.mainloop()

	def setMessage(self, event):
			if self.messageVal == 0:
				self.messageVal = 1
				self.messageVar.set("Programming is fun")
			else:
				self.messageVal = 0
				self.messageVar.set("It is fun to program")

MessageBoard()