import os
import datetime
from calendar import monthrange
from datetime import timedelta

from PIL import Image, ImageDraw, ImageFont


class WEATHER():
    def __init__(self,root_dir, renderer):
        self.assets = os.path.join(root_dir, 'assets')
        screenshotsdir = os.path.join(root_dir, 'screenshots')
        
        self.root_dir = root_dir
        self.width = 480
        self.height = 800

        self.rectangle_height = self.height/4

        self.renderer = renderer()
        
        self.clear_frame()

    def font(self,size=18):
        return ImageFont.truetype(os.path.join(self.assets, 'Font.ttc'), size)

    def clear_frame(self):
        self.Himage = Image.new('RGB', (self.width, self.height), (255,255,255))  # 255: clear the frame
        self.draw = ImageDraw.Draw(self.Himage)
        self.renderer.clear()

    def label_morning(self, current_box_top, text, c):
        heading ,value,footer = text
        self.draw.text((self.width * 0.55, (current_box_top)+(self.rectangle_height*0.2)), heading, font = self.font(18), fill = (c,c,c))
        self.draw.text((self.width * 0.55, (current_box_top)+(self.rectangle_height*0.4)), value, font = self.font(48), fill = (c,c,c))
        self.draw.text((self.width * 0.55, (current_box_top)+(self.rectangle_height*0.7)), footer, font = self.font(32), fill = (c,c,c))

    def fill_morning(self, current_box_top, color=(0, 0, 0)):
        self.draw.rectangle((0, current_box_top, self.width, current_box_top+self.rectangle_height), fill=color)

    def run(self, year=datetime.datetime.now().year, month=datetime.datetime.now().month):
        grad_ratio = 63
        cur_color = 255
        
        cur_color -= grad_ratio
        self.fill_morning(0,(192, 192, 192))
        self.label_morning(0, ("MORNING","-1°","Sunny"), 0)

        cur_color -= grad_ratio
        self.fill_morning(self.rectangle_height,(129, 129, 129))
        self.label_morning(self.rectangle_height, ("DAY","+3°","Mostly Sunny"), 255)

        cur_color -= grad_ratio
        self.fill_morning(self.rectangle_height*2,(63, 63, 63))
        self.label_morning(self.rectangle_height*2, ("EVENING","0°","Rainy"), 255)

        cur_color -= grad_ratio
        self.fill_morning(self.rectangle_height*3,(0, 0, 0))
        self.label_morning(self.rectangle_height*3, ("NIGHT","-2°","Cloudy"), 255)

        self.renderer.draw(self.Himage)