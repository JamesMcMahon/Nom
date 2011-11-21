# Indexs are designed for a single machine / enviroment
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

		lineNumber = self._findLine(file)
		if lineNumber is not None:
			return True
		return False
	
	def remove(self, file):
		# probably not the most efficent thing to seek twice
		# can replace in the future

		lineNumber = self._findLine(file)
		if lineNumber is not None:
			self._removeLine(file, lineNumber)

	def replace(self, file):
		pass

	def _findLine(self, file, full = True):
		absPath = os.path.abspath(file)		

		lineNumber = 0
		with open(self.indexPath, 'r') as index:
			for line in index:
				full, name = line.split(self.delimiter)
				if full and absPath == full:
					return lineNumber
				elif not full and file == name:
					return lineNumber
				lineNumber += 1
		return None

	# taken from http://stackoverflow.com/questions/2329417/2329972#2329972
	def _removeLine(self, filename, lineno):
		fro = open(filename, "rb")
		frw = open(filename, "r+b")

		try:
				current_line = 0
				while current_line < lineno:
					fro.readline()
					current_line += 1

				seekpoint = fro.tell()
				frw.seek(seekpoint, 0)
				print 'seekpoint ', seekpoint

				# read the line we want to discard
				fro.readline()

				# now move the rest of the lines in the file 
				# one line back 
				chars = fro.readline()
				while chars:
					frw.writelines(chars)
					chars = fro.readline()
				frw.truncate()
		finally:
				fro.close()
				frw.close()

