import os
import sys

ds = None

def cli_datastruct(dict):
	global ds
	ds = dict
	def cli_definer(name):
		def cli_decorator(fn):
			# wrapper would go here
			# print ('adding cli function ', fn)
			dict[name] = fn
			return fn
		return cli_decorator
	return cli_definer 

def dispatch(cfg):
	args = sys.argv[1:] 

	# Temp code, gets first args, dispatches
	func = ds[args[0]]
	
	args = args[1:]
	for file in args:
			if not os.path.exists(file):
				print 'invalid file ' + file
				continue
			if os.path.isdir(file):
				print "can't operate on directories " + file
				continue
			func(file, cfg)

