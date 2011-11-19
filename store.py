
class MockStore:
	def create(config):
		print ("store: create")

	def add(file):
		print ("store: add")

	def update(file):
		print ("store: update")
	
	def remove(file):
		print ("store: remove")
	
	def revert(file):
		print ("store: revert")

