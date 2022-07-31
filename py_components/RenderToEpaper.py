## sample program

#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
screenshotsdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'screenshots')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from lib.waveshare_epd import epd7in5_V2
import time
import traceback

logging.basicConfig(level=logging.DEBUG)

class RenderToEpaper():

    def __init__(self):
        self.epd = epd7in5_V2.EPD()
    
    def draw(self, image):
        try:
            logging.info("epd7in5_V2 Demo")
            
            logging.info("init and Clear")
            self.epd.init()
            self.epd.Clear()
            self.epd.display(self.epd.getbuffer(image))
            logging.info("Goto Sleep...")
            self.epd.sleep()
            
        except IOError as e:
            logging.info(e)
            
        except KeyboardInterrupt:    
            logging.info("ctrl + c:")
            epd7in5_V2.epdconfig.module_exit()
            exit()
    
    def clear(self):
        logging.info("epd7in5_V2 Demo")
        logging.info("init and Clear")
        self.epd.init()
        self.epd.Clear()
        logging.info("Goto Sleep...")
        self.epd.sleep()
