last_id = 0

class AddressEntry:
	def _init__(self, name='', street='', city='', state='', zip=''):
		self.name = name
		self.street = street
		self.city = city
		self.state = state
		self.zip = zip
		global last_id
		last_id += 1
		self.id = last_id

