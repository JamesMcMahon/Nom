import os
import shutil
import cli

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
cli = cli.cli_datastruct({})

@cli('add')
def add(file, cfg):
	if cfg.index.exists(file):
		#TODO throw error
		print "file already exists in index, can't add"
		return
 	storePath = os.path.join(cfg.storeDir, file)
	#TODO in the future allow adding of files with same names 
	if os.path.exists(storePath):
		#TODO throw error
		print "file already exists in store, can't add"
		return

	shutil.move(file, cfg.storeDir)
	os.symlink(storePath, file)
	cfg.store.add(file)
	cfg.index.add(file)

@cli('update')
def update(file, cfg):
	if not cfg.index.exists(file):
		#TODO throw error
		return
	if not os.path.islink(file):
		return 

	cfg.store.update(file)

@cli('replace')
def replace(file, cfg):
	if not cfg.index.exists(file):
		#TODO throw error
		return
	if not os.path.islink(file):
		return 

	# TODO implement
	pass

@cli('remove')
def remove(file, cfg):
	if not cfg.index.exists(file):
		#TODO throw error
		return
	if not os.path.islink(file):
		return

	cfg.index.remove(file)
	cfg.store.remove(file)

	if os.path.isdir(file):
		os.removedirs(file)
	else:
		os.remove(file)

	shutil.move(os.path.join(cfg.storeDir, file), file)

@cli('revert')
def revert(file, cfg):
	if not cfg.index.exists(file):
		#TODO throw error
		return
	if not os.path.islink(file):
		return 

	cfg.store.revert(file)

