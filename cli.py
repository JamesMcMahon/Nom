import argparse
import os
import sys

ds = None
parser = argparse.ArgumentParser(prog='nom', description='Simple storage app')

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

# FIXME this might be an abuse the type check for argparse
def file_check(filename):
	if not os.path.exists(filename):
		msg = 'invalid filename ' + filename
		raise argparse.ArgumentTypeError(msg)
	if os.path.isdir(filename):
		msg = "can't operate on directories " + filename
		raise argparse.ArgumentTypeError(msg)
	return filename

def dispatch(cfg):
	parser.add_argument('func')
	parser.add_argument('filenames', type=file_check, nargs="+")
	args = parser.parse_args()

	func = ds[args.func]
	for filename in args.filenames:
		func(filename, cfg)

