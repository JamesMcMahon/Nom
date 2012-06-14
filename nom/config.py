import os

from store import GitPythonStore
from index import FileIndex

class Config:
	nomDir = os.path.join(os.environ["HOME"], ".nom") 
	storeDir = os.path.join(nomDir, "store")
	indexName = "index"

	def __init__(self):
			# XXX both of these constructors are responsible for creating 
			# files and directories if they don't exists, 
			# might want to rethink this
			self.store = GitPythonStore(self)
			self.index = FileIndex(self)
