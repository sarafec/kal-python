from tkinter import *

class MessageBoard:
	def __init__(self):
		window = Tk()
		window.title("Message Board")
		Label(window, text="Message:").grid(row=1, column=1, sticky=W)

		self.messageVar = StringVar()
		Label(window, textvariable=self.messageVar, justify=RIGHT).grid(row=1, column=2)
		
		# todo: messages do not toggle, fix this
		window.bind("<Button-1>", self.setMessage1)
		window.bind("<Button-2>", self.setMessage2)

		window.mainloop()

	def setMessage1(self, event):
			self.messageVar.set("Programming is fun")
	
	def setMessage2(self, event):
			self.messageVar.set("It is fun to program")

MessageBoard()