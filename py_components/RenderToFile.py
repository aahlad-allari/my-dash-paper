## sample program

#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import subprocess
import platform
from os.path import exists

from PIL import Image 
import PIL

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
output = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'output')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
import traceback

logging.basicConfig(level=logging.DEBUG)

class RenderToFile():

    def __init__(self):
        self.path = output
        self.output_file = "output.png"
        self.output_file_path = os.path.join(self.path, self.output_file)
    
    def draw(self, image):
        try:
            logging.info("Writing to local file")
            # save a image using extension
            if not exists(self.path):
                os.makedirs(self.path)

            self.clear()
            im1 = image.save(self.output_file_path)
            if platform.system() == 'Darwin':
                subprocess.run(["open", self.output_file_path])
            
        except IOError as e:
            logging.info(e)
    
    def clear(self):
        logging.info("Removing File")
        if exists(self.output_file_path):
            os.remove(self.output_file_path)
