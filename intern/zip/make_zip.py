#!/bin/env/python
#-*- encoding: utf-8 -*-
"""
===============================================================================

===============================================================================

-------------------------------------------------------------------------------
"""

from __future__ import print_function
import argparse
import shutil
import sys
import os

#------------------------------------------------------------------------------

def make_zip(target_dir,mode):

	if os.path.exists(target_dir) and os.path.isdir(target_dir):

		if mode == 'all':
			files = os.listdir(target_dir)

		elif '!' in mode:
			agh = mode[1:]
			if agh == '/':
				files = [n for n in os.listdir(target_dir)\
				 	if not os.path.isdir(os.path.join(target_dir,n))]
			else:
				files = [n for n in os.listdir(target_dir) if not n.endswith(agh)]
		else:
			files = [n for n in os.listdir(target_dir) if n.endswith(mode)]

		files.remove('.DS_Store')

		for filename in files:
			shutil.make_archive(os.path.join(target_dir,filename),
				'zip',os.path.join(target_dir,filename))

#------------------------------------------------------------------------------

def main():
	parser = argparse.ArgumentParser(description='Zip Contents of Directory')
	parser.add_argument('--m',type=str,default='all',
		help='which type of file to archieve, ex: pdf, pptx)')
	parser.add_argument('--d',type=str,help='target directory')
	args = parser.parse_args()

	mode = args.m

	target_dir = args.d

	make_zip(target_dir,mode)

#------------------------------------------------------------------------------

if __name__ == "__main__":
	main()
	