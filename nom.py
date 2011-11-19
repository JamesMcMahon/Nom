#!/usr/bin/env python
# 
# nom - a program that doesn't do much yet
#

import os

class Config:
	nomDir = ".nom" #FIXME should be $HOME/nom
	storeDir = os.join(nomDir, "store")

	# XXX both of these constructors are responsible for creating 
	# files and directories if they don't exists, 
	# might want to rethink this
	store = MockStore()
	index = Index()

# in the future this might load a config
# but for now, just use the constants
cfg = Config()
dispatcher.run(cfg)
