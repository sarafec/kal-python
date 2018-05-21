from tkinter import *

class LoanCalculator:
	def __init__(self):
		window = Tk()
		window.title("Address Book")
		Label(window, text="Name").grid(row=1, column=1, columnspan=2, sticky=W)
		Label(window, text="Street").grid(row=2, column=1, columnspan=2, sticky=W)
		Label(window, text="City").grid(row=3, column=1, columnspan=2, sticky=W)
		Label(window, text="State").grid(row=3, column=3, columnspan=1)
		Label(window, text="ZIP").grid(row=3, column=5, columnspan=1)

		self.nameVar = StringVar()
		Entry(window, textvariable=self.nameVar, justify=RIGHT).grid(row=1, column=2)

		self.streetVar = StringVar()
		Entry(window, textvariable=self.streetVar, justify=RIGHT).grid(row=2, column=2)

		self.cityVar = StringVar()
		Entry(window, textvariable=self.cityVar, justify=RIGHT).grid(row=3, column=2)

		self.stateVar = StringVar()
		Entry(window, textvariable=self.stateVar).grid(row=3, column=4, columnspan=1)

		self.zipVar = StringVar()
		Entry(window, textvariable=self.zipVar).grid(row=3, column=6, columnspan=1)

		Button(window, text="Add", command=self.saveEntry).grid(row=5, column=1)
		Button(window, text="First", command=self.getFirstEntry).grid(row=5, column=2)
		Button(window, text="Next", command=self.getNextEntry).grid(row=5, column=3)
		Button(window, text="Previous", command=self.getPrevEntry).grid(row=5, column=4)
		Button(window, text="Last", command=self.getLastEntry).grid(row=5, column=5)

		window.mainloop()

	#todo: hook up buttons to  local or persistant storage
	def saveEntry(self):
		print("Entry saved!")

	def getFirstEntry(self):
		print("Fist entry!")

	def getNextEntry(self):
		print("Next entry!")

	def getPrevEntry(self):
		print("Previous entry!")

	def getLastEntry(self):
		print("Last entry!")

LoanCalculator()