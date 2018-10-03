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

ask = True

target_dir = sys.argv[1]

if os.path.exists(target_dir):
    if os.path.isdir(target_dir):
        for root, dirs, files in os.walk(target_dir, topdown=False):
            for name in files:
                if name == '.DS_Store':
                    full_path = os.path.join(root,name)
                    if ask:
                        if input("Remove {}? (y/n): ".format(full_path)) == 'y':
                            os.remove(full_path)

            for name in dirs:
                
                if name == '__pycache__':
                    full_path = os.path.join(root,name)
                    if ask:
                        if input("Remove {}? (y/n): ".format(full_path)) == 'y':
                            shutil.rmtree(full_path)