from tkinter import *
from write_db import writeToDb
from read_db import getEntryFromDb, findLastId

class AddressBook:
	def __init__(self):
		window = Tk()
		self.currentAddressId = 1
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

		self.zipVar = IntVar()
		Entry(window, textvariable=self.zipVar).grid(row=3, column=6, columnspan=1)

		Button(window, text="Add", command=self.saveEntry).grid(row=5, column=1)
		Button(window, text="First", command=self.getFirstEntry).grid(row=5, column=2)
		Button(window, text="Next", command=self.getNextEntry).grid(row=5, column=3)
		Button(window, text="Previous", command=self.getPrevEntry).grid(row=5, column=4)
		Button(window, text="Last", command=self.getLastEntry).grid(row=5, column=5)
		Button(window, text="Clear", command=self.resetUI).grid(row=5, column=6)

		window.mainloop()

	def saveEntry(self):
		writeToDb(self.nameVar.get(), self.streetVar.get(), self.cityVar.get(), self.stateVar.get(), self.zipVar.get())
		self.resetUI()

	def getFirstEntry(self):
		self.currentAddressId = 1
		idNum, targetName, targetStreet, targetCity, targetState, targetZip = getEntryFromDb(self.currentAddressId)
		self.modifyUI(targetName, targetStreet, targetCity, targetState, targetZip)

	def getNextEntry(self):
		nextId = self.setValidId(self.currentAddressId + 1)
		self.currentAddressId = nextId
		idNum, targetName, targetStreet, targetCity, targetState, targetZip = getEntryFromDb(self.currentAddressId)
		self.modifyUI(targetName, targetStreet, targetCity, targetState, targetZip)

	def getPrevEntry(self):
		prevId = self.setValidId(self.currentAddressId - 1)
		self.currentAddressId = prevId
		idNum, targetName, targetStreet, targetCity, targetState, targetZip = getEntryFromDb(self.currentAddressId)
		self.modifyUI(targetName, targetStreet, targetCity, targetState, targetZip)

	def getLastEntry(self):
		self.currentAddressId = findLastId()
		idNum, targetName, targetStreet, targetCity, targetState, targetZip = getEntryFromDb(self.currentAddressId)
		self.modifyUI(targetName, targetStreet, targetCity, targetState, targetZip)

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

	def setValidId(self, id):
		maxId = findLastId()
		if id == 0:
			return maxId
		elif id == maxId + 1:
			return 1
		else:
			return id


AddressBook()

# issues: it is easy to dupliate rows in the table by pressing add while looking through submtited entries
# improvements: create edit mode for entries that already exist