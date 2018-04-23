import datetime
last_id = 0


# deifne a note
class Note:
	def __init__(self, memo, tags=''):
		self.memo = memo
		self.tags = tags
		self.creationDate = datetime.date.today()
		global last_id
		last_id += 1
		self.__id = last_id

	def getId(self):
		return self.__id

	def match(self, filter):
		'''
		Determines if the note matches the filter text
		:param filter: Search text. Case sensitive search.
		:return: Returns True if matches, False otherwise.
		'''
		return filter in self.memo or filter in self.tags