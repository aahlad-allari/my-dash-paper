usage = '''

EPaper Python Orchestrator..

Usage:
  orchestrator.py <mode> [<value> <value1>]
'''

from docopt import docopt
import sys
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from py_components import DrawPillow
from Widgets import hacker_news_py
from Widgets.PyWidgets.py_calendar import PY_CAL
from Widgets.PyWidgets.weather import WEATHER
from Widgets.PyWidgets.dad_joke import DAD_JOKE

    

if __name__ == '__main__':
    args = docopt(usage)
    # run(args)
    
    # print(args)

    if os.uname().sysname == "Linux" and os.uname().nodename == "raspberrypi":
        from py_components.RenderToEpaper import RenderToEpaper
        renderer = RenderToEpaper
    else:
        from py_components.RenderToFile import RenderToFile
        renderer = RenderToFile

    draw = DrawPillow.DrawPillow(renderer)
    if args.get('<mode>'):
        mode = args.get('<mode>')
        if mode == 'text':
            text = args.get('<value>')
            fontsize = args.get('<value1>')
            if fontsize:
                print("fontsize")
                print(args)
                fontsize = int(fontsize)
            else:
                fontsize = 24
            if text:
                draw.draw_text(text.replace('\\n','\n'), fontsize)
            else:
                draw.draw_text("Please enter a valid text")
        elif mode == 'image':
            image_name = args.get('<value>')
            bg = args.get('<value1>')
            draw.draw_image(image_name,bg)
        elif mode == 'py_calendar':
            PY_CAL(SCRIPT_DIR).cal(grid=False, fill=True)
            draw.draw_image()
        elif mode == 'py_weather':
            WEATHER(SCRIPT_DIR, renderer).run()
            # draw.draw_image()
        elif mode == 'hackernews':
            draw.draw_text(hacker_news_py.get_text(), size=24, newline_delim="\n")
        elif mode == 'dadjoke':
            joke = DAD_JOKE()
            draw.draw_text(joke.shoot(), size=48, newline_delim="\n")
        else:
            draw.draw_text("Pease provide mode to draw..")