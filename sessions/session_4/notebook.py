from Notes import Note 

class Notebook:
	'''
	Represents a collection of notes 
	that can be modified or tagged and/or searched
	'''

	def __init__ (self):
		self.notes = []

	def new_note(self, memo, tags=''):
		n = Note(memo, tags)
		self.notes.append(n)

	def modify_memo(self, note_id, memo):
		note = self.__find_note(note_id)
		if not note:
			print("Note not found. Try again.")
		else:
			note.memo = memo

	def modify_tags(self, note_id, tags):
		note = self.__find_note(note_id)
		if not note:
			print("Note not found. Try again.")
		else:
			note.tags = tags

	def __find_note(self, note_id):
		for note in self.notes:
			if note.get() == node_id:
				return note
		return None

	def search(self, filter):
		'''
		Find all notes that match the given filter
		:param filter: filter clause
		:return: collection of notes that match the filter
		'''
		return [note for note in self.notes if note.match(filter)]