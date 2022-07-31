## sample program

#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
assets = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'assets')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
screenshotsdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'screenshots')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
from PIL import Image, ImageDraw, ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)
class DrawPillow():
    def __init__(self, renderer):
        self.width = 480
        self.height = 800

        self.font24 = ImageFont.truetype(os.path.join(assets, 'Font.ttc'), 24)
        self.font48 = ImageFont.truetype(os.path.join(assets, 'Font.ttc'), 120)
        self.font18 = ImageFont.truetype(os.path.join(assets, 'Font.ttc'), 18)

        self.renderer = renderer()

        self.clear_frame()

    def clear_frame(self):
        self.Himage = Image.new('1', (self.width, self.height), 255)  # 255: clear the frame
        self.draw = ImageDraw.Draw(self.Himage)
        self.renderer.clear()

    def draw_circle():
        pass

    def draw_text(self, input_text):
        self.clear_frame()
        self.draw.text((2, 20), input_text, font = self.font18, fill = 0)
        self.renderer.draw(self.Himage)
    
    def draw_image(self, name="image.png"):
        self.Himage = Image.open(os.path.join(screenshotsdir, 'image.png'))
        self.renderer.draw(self.Himage)

    def park(self):
        pass
        # Drawing on the Horizontal image
        # logging.info("1.Drawing on the Horizontal image...")
        # self.Himage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
        # draw = ImageDraw.Draw(self.Himage)
        # draw.text((10, 0), 'Hi My name is ', font = font48, fill = 0)
        # draw.text((10, 130), 'Tuhi  <3', font = font48, fill = 0)
        # draw.line((20, 50, 70, 100), fill = 0)
        # draw.line((70, 50, 20, 100), fill = 0)
        # draw.rectangle((20, 50, 70, 100), outline = 0)
        # draw.line((165, 50, 165, 100), fill = 0)
        # draw.line((140, 75, 190, 75), fill = 0)
        # draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
        # draw.rectangle((80, 50, 130, 100), fill = 0)
        # draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
        # epd.display(epd.getbuffer(self.Himage))
        # time.sleep(2)

        # # Drawing on the Vertical image
        # logging.info("2.Drawing on the Vertical image...")
        Limage = Image.new('1', (self.height, self.width), 255)  # 255: clear the frame
        draw = ImageDraw.Draw(Limage)
        
        # table_name = 6
        # count = 10
        # width = 0
        # for j in [5,6,7]:
        #     for i in range(10):
        #         print(f'{j} X {i+1} = {j*(i+1)}')
        #         draw.text((140*width, 25*i), f'{j} X {i+1} = {j*(i+1)}', font = font24, fill = 0)
        #     width+=1
        # draw.text((2, 20), '7.5inch epd', font = font18, fill = 0)
        # draw.text((20, 50), u'微雪电子', font = font18, fill = 0)
        # draw.line((10, 90, 60, 140), fill = 0)
        # draw.line((60, 90, 10, 140), fill = 0)
        # draw.rectangle((10, 90, 60, 140), outline = 0)
        # draw.line((95, 90, 95, 140), fill = 0)
        # draw.line((70, 115, 120, 115), fill = 0)
        # draw.arc((70, 90, 150, 140), 0, 360, fill = 0)
        # draw.rectangle((10, 150, 60, 200), fill = 0)
        # draw.chord((70, 150, 120, 200), 0, 360, fill = 0)
        # epd.display(epd.getbuffer(Limage))
        # time.sleep(2)

        # logging.info("3.read bmp file")
        # self.Himage = Image.open(os.path.join(assets, 'wolv.jpeg'))
        # self.Himage = Image.open(os.path.join(assets, 'Tuhi.jpg'))
        # self.Himage = Image.open(os.path.join(assets, 'santa.jpg'))
        # self.Himage = Image.open(os.path.join(assets, 'collage.jpg'))
        # # self.Himage = Image.open(os.path.join(assets, 'eink_sample/chicago.jpeg'))
        # # self.Himage = Image.open(os.path.join(assets, 'eink_sample/elephant.png'))
        # self.Himage = Image.open(os.path.join(assets, 'eink_sample/poster-2.jpeg'))
        # # self.Himage = Image.open(os.path.join(assets, 'eink_sample/news.jpeg'))

        self.Himage = Image.open(os.path.join(screenshotsdir, 'image.png'))
        # epd.display(epd.getbuffer(self.Himage))
        # time.sleep(2)

        # logging.info("4.read bmp file on window")
        # self.Himage2 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
        # bmp = Image.open(os.path.join(assets, '100x100.bmp'))
        # self.Himage2.paste(bmp, (50,10))
        # epd.display(epd.getbuffer(self.Himage2))
        # time.sleep(2)