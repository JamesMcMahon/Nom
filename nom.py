#!/usr/bin/env python
# 
# nom - a program that doesn't do much yet
#

import os

class Config:
	repo = "test-repo" #TODO change
	store = MockStore()
	index = Index()

def _setup(cfg):
	#TODO make the repo if it does exist
	cfg.store.create(cfg)	

# in the future this might load a config
# but for now, just use the constants
cfg = Config()

if not os.path.exists(cfg.repo):
	_setup(cfg)

dispatcher.run(cfg)
