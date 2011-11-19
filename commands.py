import os
import shutil

"""
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
"""

def add(file, cfg):
	if cfg.index.exists(file):
		#TODO throw error
		pass

	shutil.move(file, config.repo)
	os.symlink(os.join(config.repo, file), file)
	cfg.store.add(file)
	cfg.index.add(file)

def update(file, cfg):
	if not cfg.index.exists(file):
		#TODO throw error
		pass

	cfg.store.update(file)

def replace(file, cfg):
	if cfg.index.exists(file):
		#TODO throw error
		pass

	# TODO implement
	pass

def remove(file, cfg):
	if not cfg.index.exists(file):
		#TODO throw error
		pass

	# TODO implement
	pass

def revert(file, cfg):
	if not cfg.index.exists(file):
		#TODO throw error
		pass

	cfg.store.revert(file)

