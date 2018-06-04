from tkinter import *
from entry import AddressEntry

class AddressBook:
	def __init__(self):
		self.entries = []
		self.currentEntry = 0
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
		Button(window, text="Clear", command=self.resetUI).grid(row=5, column=6)

		window.mainloop()

	def saveEntry(self):
		#todo: use address entry class instead of plain list
		# addressEntry = AddressEntry(self.nameVar.get(), self.streetVar.get(), self.cityVar.get(), self.stateVar.get(), self.zipVar.get())
		addressEntry = [self.nameVar.get(), self.streetVar.get(), self.cityVar.get(), self.stateVar.get(), self.zipVar.get()]
		self.entries.append(addressEntry)
		self.resetUI()

	def getFirstEntry(self):
		targetName, targetStreet, targetCity, targetState, targetZip = self.entries[0]
		self.modifyUI(targetName, targetStreet, targetCity, targetState, targetZip)
		self.currentEntry = 0

	def getNextEntry(self):
		if (self.currentEntry + 1) > (len(self.entries) - 1):
			self.currentEntry = 0
		else:
			self.currentEntry += 1

		targetName, targetStreet, targetCity, targetState, targetZip = self.entries[self.currentEntry]
		self.modifyUI(targetName, targetStreet, targetCity, targetState, targetZip)


	def getPrevEntry(self):
		if (self.currentEntry - 1) < 0:
			self.currentEntry = (len(self.entries) - 1)
		else:
			self.currentEntry -= 1

		targetName, targetStreet, targetCity, targetState, targetZip = self.entries[self.currentEntry]
		self.modifyUI(targetName, targetStreet, targetCity, targetState, targetZip)

	def getLastEntry(self):
		numberOfEntries = len(self.entries)
		targetName, targetStreet, targetCity, targetState, targetZip = self.entries[numberOfEntries - 1]
		self.modifyUI(targetName, targetStreet, targetCity, targetState, targetZip)
		self.currentEntry = numberOfEntries - 1

	def modifyUI(self, targetName, targetStreet, targetCity, targetState, targetZip):
		self.nameVar.set(targetName)
		self.streetVar.set(targetStreet)
		self.cityVar.set(targetCity) 
		self.stateVar.set(targetState)
		self.zipVar.set(targetZip)

	def resetUI(self):
		self.nameVar.set('')
		self.streetVar.set('')
		self.cityVar.set('') 
		self.stateVar.set('')
		self.zipVar.set('')



AddressBook()