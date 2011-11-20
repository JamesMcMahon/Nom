import os

class MockStore:
	def __init__(self, cfg):
		if not os.path.exists(cfg.storeDir):
			self._create(cfg)

	def add(self, file):
		print ("store: add")

	def update(self, file):
		print ("store: update")
	
	def remove(self, file):
		print ("store: remove")
	
	def revert(self, file):
		print ("store: revert")

	def _create(self, cfg):
		print ("store: create")
		os.makedirs(cfg.storeDir)

