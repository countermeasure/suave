import curses
import subprocess

from grid import Grid


class Box(object):
    """
    Manages the drawing and refreshing of boxes.
    """

    def __init__(self, screen, height, width, origin_y=0, origin_x=0,
                 contents=None):
        # Set box colors.
        foreground = curses.COLOR_BLACK
        background = curses.COLOR_WHITE
        curses.init_pair(1, foreground, background)

        # Set attributes.
        self.screen = screen
        self.grid = Grid(screen)
        self.height = height
        self.width = width
        self.origin_y = origin_y
        self.origin_x = origin_x
        self.contents = contents

        # Create the box and set its colors.
        self.box = curses.newwin(
            self.grid.height(self.height),
            self.grid.width(self.width),
            self.grid.origin_y(self.origin_y),
            self.grid.origin_x(self.origin_x)
        )
        self.box.bkgdset(ord(' '), curses.color_pair(1))
        self.box.addstr(subprocess.check_output(self.contents, shell=True))

    def refresh(self):
        """
        Rerenders the box.
        """
        # Refresh the grid and re-calculate the box's size and position.
        self.grid.refresh()
        height = self.grid.height(self.height)
        width = self.grid.width(self.width)
        origin_x = self.grid.origin_x(self.origin_x)
        origin_y = self.grid.origin_y(self.origin_y)

        # Refresh the box.
        self.box.erase()
        self.box.mvwin(origin_y, origin_x)
        self.box.resize(height, width)
        self.box.addstr(subprocess.check_output(self.contents, shell=True))
        self.box.refresh()
