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
	os.symlink(storePath, file.rstrip('/\\'))
	cfg.store.add(file)
	cfg.index.add(file)

@cli('update')
def update(file, cfg):
	if not cfg.index.exists(file):
		print "file does not exist in the index, can't update"
		#TODO throw error
		return
	if not os.path.islink(file):
		print "file is not a link, can't update"
		return 

	cfg.store.update(file)

#@cli('replace')
def replace(file, cfg):
	if cfg.index.exists(file):
		#TODO throw error
		print "file already exists in index, can't replace"
		return

	# TODO implement
	pass

@cli('remove')
def remove(file, cfg):
	if not cfg.index.exists(file):
		#TODO throw error
		print "file does not exist in the index, can't remove"
		return
	if not os.path.islink(file):
		print "file is not a link, can't remove"
		return

	cfg.index.remove(file)
	cfg.store.remove(file)
	os.remove(file)
	shutil.move(os.path.join(cfg.storeDir, file), file)

@cli('revert')
def revert(file, cfg):
	if not cfg.index.exists(file):
		#TODO throw error
		print "file does not exist in the index, can't revert"
		return
	if not os.path.islink(file):
		print "file is not a link, can't revert"
		return 

	cfg.store.revert(file)

