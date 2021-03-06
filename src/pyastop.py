# -*- coding: utf8 -*-

import argparse
import sys
import astop
import os
import ast
from astop import codegen

# c = ast.parse("with a as b: print b", "noname")
# print dir(c)
# print ast.dump(c)

print codegen.to_source(ast.Repr(ast.Num(1)))

def main():
	args = parseArgs(sys.argv[1:])

	# convert directories to filenames
	sources = list(args.sources)
	for dir in args.directory or []:
		sources += getSourcesInDirectory(dir)

	astop.astoptimize( sources )

def parseArgs(args):
	parser = argparse.ArgumentParser(
		prog="pyastop.py",
		description="Python AST Optimizer by Nan Lin @NeteaseGames",
		# usage='%(prog)s [options]'
	)

	# parser.add_argument('-o', '--output', nargs=1, metavar="<file>", type=str, required=True, help="specify the output source file")
	parser.add_argument('-d', '--directory', metavar="<dir>", type=str, nargs=1, help="specify input source directory")
	parser.add_argument('sources', metavar="<sources>", type=str, nargs='*', help="input source files")
	return parser.parse_args(args)

def getSourcesInDirectory(srcdir, ignore_dirs=('.svn', '.git')):
	sources = []
	for path, dirs, files in os.walk(srcdir):
		for igdir in ignore_dirs:
			if igdir in dirs: dirs.remove(igdir)
		for fn in files:
			if fn.endswith('.py'):
				sources.append(os.path.join(path, fn))

	return sources

if __name__ == '__main__':
	main()
