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
from PIL import Image, ImageDraw, ImageFont, ImageOps
import traceback

logging.basicConfig(level=logging.ERROR)
class DrawPillow():
    def __init__(self, renderer):
        self.width = 800
        self.height = 480


        self.font18 = ImageFont.truetype(os.path.join(assets, 'Font.ttc'), 18)
        self.font24 = ImageFont.truetype(os.path.join(assets, 'Font.ttc'), 24)
        self.font48 = ImageFont.truetype(os.path.join(assets, 'Font.ttc'), 48)
        self.font72 = ImageFont.truetype(os.path.join(assets, 'Font.ttc'), 72)

        self.renderer = renderer()

        self.clear_frame()

    def clear_frame(self):
        self.Himage = Image.new('1', (self.width, self.height), 255)  # 255: clear the frame
        self.draw = ImageDraw.Draw(self.Himage)
        self.renderer.clear()

    def draw_circle():
        pass

    def get_fonts(self,size=18, style='Font.ttc'):
        return ImageFont.truetype(os.path.join(assets, style), size)

    def draw_text(self, input_text, size=24, orientation="L", newline_delim="\n"):
        # based on orientation render text rotate 90 degrees
        if orientation == "P":
            self.width = 480
            self.height = 800
            self.Himage = Image.new('1', (self.width, self.height), 255)
            self.draw = ImageDraw.Draw(self.Himage)
            self.Himage = self.Himage.rotate(90, expand=1)
        else:
            self.width = 800
            self.height = 480
            self.Himage = Image.new('1', (self.width, self.height), 255)
            self.draw = ImageDraw.Draw(self.Himage)


        font_size = self.get_fonts(18)
        line_size = 20
        if size == 18:
            font_size = self.get_fonts(18)
            line_size = 20
        elif size == 24:
            font_size = self.get_fonts(24)
            line_size = 26
        elif size == 48:
            font_size = self.get_fonts(48)
            line_size = 50
        elif size == 72:
            font_size = self.get_fonts(72)
            line_size = 74
        else:
            font_size = self.get_fonts(120)
            line_size = 122
        line_no = 0
        if(newline_delim == "word"):
            words = input_text.split()
        else:
            words = input_text.split("\n")
        
        for sentense in words:
            wrapped_sentence = self.visual_split(sentense, font_size, self.width)
            if len(wrapped_sentence) > 1:
                for wrd in wrapped_sentence:
                    self.draw.text((2, line_no*line_size), wrd, font = font_size, fill = 0)
                    line_no +=1
            else:
                self.draw.text((2, (line_no*line_size)), sentense, font = font_size, fill = 0)
                line_no +=1

            self.draw.text((2, (line_no*line_size)), "\n", font = font_size, fill = 0)
            line_no +=1
        self.renderer.draw(self.Himage)
    
    def draw_image(self, name="image.png", bg="WHITE"):
        if bg == 'undefined':
            b = "WHITE"
        else:
            b = bg
        if name == 'undefined':
            n = "image.png"
        else:
            n = name
        self.Himage = Image.open(os.path.join(screenshotsdir, n))
        w = self.width
        h = self.height

        iw, ih = self.Himage.size

        # If dimentions of image are inverted you need to convert from portrait to width
        if iw < ih:
            w = self.height
            h = self.width
        
        self.Himage.thumbnail(size=(w,h), resample=Image.ANTIALIAS)
        
        # FIll transparant background with white]
        new_image = Image.new("RGBA", (w,h), b) # Create a white rgba background
        new_image.paste(self.Himage, (0, 0), self.Himage)              # Paste the image on the background. Go to the links given below for details.
        # new_image.convert('RGB').save('test.jpg', "JPEG")  # Save as JPEG
        
        
        self.renderer.draw(new_image.convert('1'))

    def invert_image_color(self, image):
        if image.mode == 'RGBA':
            r,g,b,a = image.split()
            rgb_image = Image.merge('RGB', (r,g,b))
            inverted_image = ImageOps.invert(rgb_image)
            r2,g2,b2 = inverted_image.split()
            final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))
            return final_transparent_image
        else:
            inverted_image = ImageOps.invert(image)
            return inverted_image

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

        from PIL import ImageFont

    def visual_split(self, text, font, width, response_type='list'):
        font = font
        words = text.split()
        
        word_lengths = [(word, font.getsize(word)[0]) for word in words]
        space_length = font.getsize(' ')[0]
        
        lines = ['']
        line_length = 0
        
        for word, length in word_lengths:

            if line_length+length <= width:
                lines[-1] = '{line}{word} '.format(line=lines[-1], word=word)
                line_length += length + space_length
            else:
                lines.append('{word} '.format(word=word))
                line_length = length + space_length
        
        if response_type == 'list':
            return [line.strip() for line in lines]
        elif response_type == 'str':
            return '\n'.join(line.strip() for line in lines)
        else:
            raise ValueError('Invalid response type. Valid values are "list" and "str".')
        