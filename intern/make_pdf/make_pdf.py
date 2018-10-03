#!/bin/env/python
#-*- encdoing: utf-8 -*-
"""
===============================================================================

===============================================================================

-------------------------------------------------------------------------------
"""
import comtypes.client
import argparse
import shutil
import sys
import os

DIR = "C:/Users/soffer/Desktop/Slides_PPT_CN_Rename (huiyanx.cao@intel.com )/"

class PPTX2PDF():

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--dir', type=str, help='root of pptx',
            default=DIR)
        self.args = parser.parse_args()

    #------------------------------------------------------------------------------

    def convert(self,inputFileName, outputFileName, formatType = 32):
        powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
        powerpoint.Visible = 1

        if outputFileName[-3:] != 'pdf':
            outputFileName = outputFileName + ".pdf"

        print(inputFileName)

        deck = powerpoint.Presentations.Open(inputFileName)
        deck.SaveAs(outputFileName, formatType) 
        deck.Close()
        powerpoint.Quit()

    #------------------------------------------------------------------------------

    def walk_dir(self,dir_path):
        dir_path = dir_path.replace('/',os.sep)
        for root, dirs, files in os.walk(dir_path, topdown=False):
           for name in files:
              target = os.path.join(root, name)
              if target.endswith('.pptx'):
                output_path = target.split(".pptx")[0]+'.pdf'
                if not os.path.exists(output_path):
                    print(target)
                    self.convert(target,output_path)
                    print(output_path)

    #------------------------------------------------------------------------------

    def main(self):
        target_dir = self.args.dir 
        if not os.path.exists(target_dir):
            raise SystemError("Target directory arg does not exist: {}".format(target_dir))

        if not os.path.isdir(target_dir):
            raise SystemError("Target directory arg is not a directory: {}".format(target_dir))

        self.walk_dir(target_dir)


def format_folder(dir_path):

    for root, dirs, files in os.walk(dir_path, topdown=False):
        for name in files:
            print(name)

            target = os.path.join(root, name)
            if target.endswith('.pdf'):
                print(target)
                id_num = os.listdir(os.path.dirname(target)).index(os.path.basename(target))
                temp = os.path.join(os.path.dirname(target),"Week_{}".format(id_num))
                os.mkdir(temp)
                shutil.move(target,os.path.join(temp,os.path.basename(target)))


def remove_pptx(dir_path):

    for root, dirs, files in os.walk(dir_path, topdown=False):
        for name in files:
            print(name)
            if name.endswith('.pptx'):
                #print(os.path.join(root,name))
                os.remove(os.path.join(root,name))

            #target = os.path.join(root, name)
            #if target.endswith('.pdf'):
            #    print(target)
            ##    id_num = os.listdir(os.path.dirname(target)).index(os.path.basename(target))
            #    temp = os.path.join(os.path.dirname(target),"Week_{}".format(id_num))
            #    os.mkdir(temp)
            #    shutil.move(target,os.path.join(temp,os.path.basename(target)))

def main():
    target_dir = sys.argv[1]

    if not os.path.exists(target_dir):
        raise SystemError("Target directory arg does not exist: {}".format(target_dir))

    if not os.path.isdir(target_dir):
        raise SystemError("Target directory arg is not a directory: {}".format(target_dir))

    format_folder(target_dir)


if __name__ == "__main__":
    PPTX2PDF().main()
    #format_folder()
    #emove_pptx()