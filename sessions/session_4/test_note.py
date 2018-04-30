import sys
from notebook import Notebook, Note

class Menu:
	def __init__(self):
		self.notebook = Notebook()
		self.choices = {
			"1": self.show_notes,
			"2": self.search_notes,
			"3": self.add_note,
			"4": self.modify_note,
			"5": self.quit
		}

	def display_menu(self):
		print("""
		Notebook Menu

		1. Show all notes
		2. Search notes 
		3. Add note 
		4. Modify note 
		5. Quit
		""")

	def run(self):
		while True:
			self.display_menu()
			choice = input("Enter an option: ")
			action = self.choices.get(choice)
			if action:
				action()
			else:
				print("{0} is note a valid choice".format(choice))


	def quit(self):
		print("Thank you for using the notebook.")
		sys.exit(0)

	def add_note(self):
		memo = input("Enter a memo: ")
		self.notebook.new_note(memo)
		print("Your note has been added.")


	def search_notes(self):
		filter = input("Search for: ")
		notes = self.notebook.search(filter)
		self.show_notes(notes)

	def modify_note(self):
		id = int(input("Enter a node id: "))
		memo = input("Enter a memo: ")
		tags = input("Enter tags: ")

		if memo:
			self.notebook.modify_memo(id, memo)

		if tags:
			self.notebook.modify_tags(id, tags)

	def show_notes(self, notes=None):
		if not notes:
			notes = self.notebook.notes 

		for note in notes:
			print("{0}: {1} \n{2} ".format(note.getId(), note.memo, note.tags))

menu = Menu()
menu.run()