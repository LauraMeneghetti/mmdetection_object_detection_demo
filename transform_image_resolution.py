# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:57:02 2019

@author: MenegLau
"""

from PIL import Image
from os import listdir, path
import argparse

def rescale_images(directory, size):
    for img in listdir(directory):
    	  img_path = path.join(directory, img)
    	  img_name, img_ext = path.splitext(img)
    	  if img_ext.lower() != '.xml':
    	  	   #break
    	  #else:
        #if img_ext.lower() == '.xml':
         #   break
        #else:
            im = Image.open(directory+img)
            im_resized = im.resize(size, Image.ANTIALIAS)
            im_resized.save(directory+img)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rescale images")
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the images')
    parser.add_argument('-s', '--size', type=int, nargs=2, required=True, metavar=('width', 'height'), help='Image size')
    args = parser.parse_args()
    rescale_images(args.directory, args.size)