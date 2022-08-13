usage = '''

EPaper Python Orchestrator..

Usage:
  orchestrator.py <mode> [<value>]
'''

from docopt import docopt
import sys
import os


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from py_components import DrawPillow
from Widgets import hacker_news_py
from Widgets.PyWidgets.py_calendar import PY_CAL

    

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
            if text:
                draw.draw_text(text, 18)
            else:
                draw.draw_text("Please enter a valid text")
        elif mode == 'image':
            draw.draw_image()
        elif mode == 'py_calendar':
            PY_CAL(SCRIPT_DIR).cal(grid=False, fill=True)
            draw.draw_image()
        elif mode == 'hackernews':
            draw.draw_text(hacker_news_py.get_text(), size=24, newline_delim="\n")
        else:
            draw.draw_text("Pease provide mode to draw..")