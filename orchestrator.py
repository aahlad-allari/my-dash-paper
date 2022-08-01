import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from py_components import DrawPillow
from Widgets import hacker_news_py

if os.uname().sysname == "Linux" and os.uname().nodename == "raspberrypi":
    from py_components.RenderToEpaper import RenderToEpaper
    renderer = RenderToEpaper
else:
    from py_components.RenderToFile import RenderToFile
    renderer = RenderToFile


draw = DrawPillow.DrawPillow(renderer)
# draw.draw_text("Hello How are you? are you feeling well")
draw.draw_image()
# draw.draw_text(hacker_news_py.get_text(), size=18, newline_delim="\n")
