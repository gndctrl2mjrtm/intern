from __future__ import print_function
import argparse
import shutil
import sys
import os

target_dir = sys.argv[1]

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--m',type=str,default='all',
	help='mode for making zip (which type of file to archieve, ex: pdf, pptx)')
parser.add_argument('--d',type=str,help='target directory')
args = parser.parse_args()

mode = args.m

target_dir = args.d

if os.path.exists(target_dir) and os.path.isdir(target_dir):

	if mode == 'all':
		files = os.listdir(target_dir)
		files.remove('.DS_Store')
		print(files)
	else:
		files = [n for n in os.listdir(target_dir) if n.endswith(mode)]



	for filename in files:
		shutil.make_archive(os.path.join(target_dir,filename),'zip',os.path.join(target_dir,filename))