
class MockStore:
	def __init__(self, cfg):
		# TODO create if store doesn't exist
		pass

	def add(self, file):
		print ("store: add")

	def update(self, file):
		print ("store: update")
	
	def remove(self, file):
		print ("store: remove")
	
	def revert(self, file):
		print ("store: revert")

	def _create(self, config):
		print ("store: create")
