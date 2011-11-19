import os
import shutil

# TODO make file absolute path, os.path.abspath

class vcs:
	def add(toAdd):
		pass

	def update(toUpdate):
		pass
	
	def revert(toRevert):
		pass

class config:
	repo = "test-repo"
	vcs = vcs()

def checkFile(file):
	if not os.path.isfile(file):
		# TODO throw error
		return

	# TODO things to check;
	# 1. Does the file exist
	# 2. Do we have access to the file
	# 3. Is the file a symlink
	# 4. Is the file a file or directory
	pass

def addOrUpdate(file, config):
	stored = os.join(config.repo, file)
	 
	if os.path.exists(stored):
		update(stored, config.vcs)
	else:
		add(file, config)

def add(toAdd, config):
	shutil.move(file, config.repo)
	os.symlink(os.join(config.repo, file), file)
	config.vcs.add(file)

def update(toUpdate, vcs):
	# Do we need this method?
	vcs.update(toUpdate)

def remove(toRemove, vcs):
	# TODO implement
	pass

def revert(toRevert, vcs):
	# TODO implement
	pass
