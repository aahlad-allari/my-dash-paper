import os
import datetime
from calendar import monthrange
from datetime import timedelta

import matplotlib
import matplotlib.patches as patches
import matplotlib.pyplot as plt

class PY_CAL():
    def __init__(self,root_dir):
        self.root_dir = root_dir
        self.fillday_list = [(datetime.datetime.now().month, datetime.datetime.now().day)]

        # Japanese holiday
        self.holiday_list = [
            (1, 1),
            (1, 10),
            (2, 11),
            (2, 23),
            (3, 21),
            (4, 29),
            (5, 3),
            (5, 4),
            (5, 5),
            (7, 18),
            (8, 11),
            (9, 19),
            (9, 23),
            (10, 10),
            (11, 3),
            (11, 23),
        ]

        # self.cal( grid=False, fill=False)

    def label_month(self,year, month, ax, i, j, cl="black"):
        months = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]

        month_label = f"{months[month-1]} {year}"
        ax.text(i, j, month_label, color=cl, va="center")


    def label_weekday(self,ax, i, j, cl="black"):
        x_offset_rate = 1
        for weekday in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]:
            ax.text(i, j, weekday, ha="center", va="center", color=cl)
            i += x_offset_rate


    def label_day(self,ax, day, i, j, cl="black"):

        ax.text(i, j, int(day), ha="center", va="center", color=cl)


    def fill_box(self,ax, i, j):
        ax.add_patch(
            patches.Rectangle(
                (i - 0.5, j - 0.5),
                1,
                1,
                edgecolor="black",
                facecolor="black",
                alpha=1,
                fill=True,
            )
        )
    
    def fill_circle(self,ax, i, j):
        ax.add_patch(
            patches.Circle(
                (i, j),
                radius=0.35,
                edgecolor="black",
                facecolor="black",
                alpha=1,
                fill=True,
            )
        )


    def check_fill_day(self,year, month, day, weekday):
        if (month, day) in self.fillday_list:
            return True


    def check_color_day(self,year, month, day, weekday):
        if (month, day) in self.holiday_list:
            return "red"
        
        if (month, day) in self.fillday_list:
            return "white"

        if weekday == 6:  # Sunday
            return "red"
        
        if weekday == 5:  # Saturday
            return "blue"

        return "black"


    def month_calendar(self,ax, year, month, fill):
        date = datetime.datetime(year, month, 1)

        weekday, num_days = monthrange(year, month)

        # adjust by 0.5 to set text at the ceter of grid square
        x_start = 1 - 0.5
        y_start = 5 + 0.5
        x_offset_rate = 1
        y_offset = -1

        self.label_month(year, month, ax, x_start, y_start + 2)
        self.label_weekday(ax, x_start, y_start + 1)

        j = y_start

        for day in range(1, num_days + 1):
            i = x_start + weekday * x_offset_rate
            color = self.check_color_day(year, month, day, weekday)

            if fill and self.check_fill_day(year, month, day, weekday):
                # self.fill_box(ax, i, j)
                self.fill_circle(ax, i, j)

            self.label_day(ax, day, i, j, color)
            weekday = (weekday + 1) % 7
            if weekday == 0:
                j += y_offset


    def cal(self, year=datetime.datetime.now().year, month=datetime.datetime.now().month, grid=False, fill=False):
        fig = plt.figure()
        plt.rcParams.update({'font.size': 14})
        ax = fig.add_subplot()
        ax.axis([0, 7, 0, 7])
        ax.axis("off")

        if grid:
            ax.axis("on")
            ax.grid(grid)
            for tick in ax.xaxis.get_major_ticks():
                tick.tick1line.set_visible(False)
                tick.tick2line.set_visible(False)
                tick.label1.set_visible(False)
                tick.label2.set_visible(False)

            for tick in ax.yaxis.get_major_ticks():
                tick.tick1line.set_visible(False)
                tick.tick2line.set_visible(False)
                tick.label1.set_visible(False)
                tick.label2.set_visible(False)
        self.month_calendar(ax, year, month, fill)
        # plt.show()

        screenshot_dir = os.path.join(self.root_dir, 'screenshots')
        h = int(800)
        w = int(480)
        wi, hi = fig.get_size_inches()
        fig.set_size_inches(hi*(w/h), hi)
        plt.savefig(os.path.join(screenshot_dir, 'image.png'),format='png',
            dpi=h/hi, bbox_inches='tight',  pad_inches=0.1)
