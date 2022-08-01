import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from py_components import DrawPillow
from Widgets import hacker_news_py
from Widgets.PyWidgets.py_calendar import PY_CAL

if os.uname().sysname == "Linux" and os.uname().nodename == "raspberrypi":
    from py_components.RenderToEpaper import RenderToEpaper
    renderer = RenderToEpaper
else:
    from py_components.RenderToFile import RenderToFile
    renderer = RenderToFile


draw = DrawPillow.DrawPillow(renderer)
# draw.draw_text("Hello How are you? are you feeling well")

PY_CAL(SCRIPT_DIR).cal(year = 2022, month = 8, grid=False, fill=True)
draw.draw_image()
# draw.draw_text(hacker_news_py.get_text(), size=18, newline_delim="\n")
