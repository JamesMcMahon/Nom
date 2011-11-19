import sys

def cli_datastruct(dict):
	def cli_definer(name):
		def cli_decorator(fn):
			# wrapper would go here
			print ('adding cli function ', fn)
			dict[name] = fn
			return fn
		return cli_decorator
	return cli_definer 

def run(cfg):
	args = sys.argv[1:] 
	# TODO interpret command line options and dispatch
	pass
