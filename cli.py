import argparse
import os
import sys

ds = None
helpDs = {}
parser = argparse.ArgumentParser(prog='nom', description='Simple storage app')

def cli_datastruct(dict):
	global ds
	ds = dict
	def cli_definer(name, help=None):
		def cli_decorator(fn):
			# wrapper would go here
			# print ('adding cli function ', fn, help)
			dict[name] = fn
			helpDs[name] = help
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
	sub = parser.add_subparsers(help='sub-command help')
	for fnName, fn in ds.items():
		fp = sub.add_parser(fnName, help=helpDs[fnName])
		fp.set_defaults(func=fn)

		# add filesnames to each sub argument
		# currently this is needed by each command
		fp.add_argument('filenames', type=file_check, nargs="+")

	args = parser.parse_args()
	func = args.func
	for filename in args.filenames:
		func(filename, cfg)

