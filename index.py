# Indexs are design for a single machine / enviroment
# and will NOT be version controlled

# index - file full path to file name (entry in VCS)
# allows reverse lookup from sim links 

import os

class Index:
	delimiter = '|'

	def __init__(self, cfg):
		self.indexPath = os.path.join(cfg.nomDir, cfg.indexName)

		if not os.path.exists(self.indexPath):
				open(self.indexPath, 'w').close()

	def add(self, file):
		absPath = os.path.abspath(file)		

		with open(self.indexPath, 'w') as index:
			# FIXME is there a constant for end of line in python?
			index.write(absPath + self.delimiter + file + '\n')

	def exists(self, file):
		absPath = os.path.abspath(file)		

		with open(self.indexPath, 'r') as index:
			for line in index:
				key, value = line.split(self.delimiter)
				if absPath == key:
					return True
		return False	
	
	def remove(self, file):
		absPath = os.path.abspath(file)		

		pass
		"""
		with open(self.indexPath, 'w') as index:
			for line in index:
				key, value = line.split(self.delimiter)
				if absPath == key:
					return True
		"""
		# throw error if entry not found?

	def replace(self, file):
		pass

