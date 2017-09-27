import sqlite3


# outsourcing the database operations.
class db:
	"""class that organizes db"""

	def __init__(self):
		# create/connnect to database and table
		self.db = sqlite3.connect('settings.db')
		self.db.row_factory = sqlite3.Row
		# saves the settings
		self.db.execute('''CREATE TABLE IF NOT EXISTS settings
                            (game text, name text, lang text, rx integer, ry integer, 
                            fs integer, bl integer, mods text, dlc text)''')

	def new(self, **kwargs):
		""" insert new settings, takes arguments as **kwargs"""
		# making a string of values for sqlite statement
		settings = ""
		for key, value in kwargs.items():
			if isinstance(value, str):
				settings += "'" + value + "', "
			if isinstance(value, int):
				settings += str(value) + ", "
			elif isinstance(value, list):
				settings += "'" + ','.join(value) + "',"
		# print(settings)
		if settings[-1] == ' ':
			settings = settings[:-2]
		elif settings[-1] == ',':
			settings = settings[:-1]
		# there is more elegant ways of doing this ...
		# inserting a new set of settings into our db
		insert = ('insert into settings (game,name,lang,rx,ry,fs,bl,mods,dlc) values (' + settings + ')')
		print (insert)
		self.db.execute(insert)
		self.db.commit()

	def check(self, game, name):
		""" checks if settings with name exists for given game"""
		cursor = self.db.execute('select name from settings where game = ? and name = ?', (game, name))
		list = cursor.fetchall()
		if not list:
			return False
		else:
			return True

	def delete(self, name, game):
		"""find setting for name and game and delete!"""
		self.db.execute('delete from settings where game = ? and name = ?', (game, name))
		self.db.commit()

	def list(self):
		"""lists everything"""
		self.db.execute('select * from settings')
		self.db.commit()

	def get(self, name, game):
		"""returns database entry for name and game"""
		set = self.db.execute('select * from settings where game = ? and name = ?', (game, name))
		return dict(set.fetchone())

	def close(self):
		self.db.close()

	def __iter__(self):
		rows = self.db.execute('select * from settings')
		for row in rows:
			yield dict(row)


# main will only be executed if main-module -> for test runs

# db module for settings selector -> will not be executed

def main():
	test = db()

	print('Create rows')
	test.new(game = 'Europa Universalis IV', name='name', lang='german', rx=1920, ry=1080, fs=0, bl=1, mods='', dlc='')
	test.new(game = 'Stellaris', name='really', lang='english', rx=1920, ry=1080, fs=0, bl=1, mods='', dlc='')
	for row in test:
		print(row)

	print('Retrieve rows')
	print(test.get('Europa Universalis IV', 'name'))

	print('Delete rows')
	test.delete('Stellaris', 'really')
	for row in test:
		print(row)


if __name__ == "__main__":
	main()
