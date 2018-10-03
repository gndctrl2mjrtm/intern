#!/bin/env/python
#-*- encdoing: utf-8 -*-
"""
===============================================================================

===============================================================================

-------------------------------------------------------------------------------
"""
from __future__ import print_function
from __future__ import division
import shutil
import sys
import os

def remove_pptx():

    dir_path = "C:\\Users\\soffer\\Desktop\\Chinese_Courses_Student_Version"

    for root, dirs, files in os.walk(dir_path, topdown=False):
        for name in files:
            print(name)
            if name.endswith('.pptx'):
                #print(os.path.join(root,name))
                os.remove(os.path.join(root,name))