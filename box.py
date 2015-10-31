import curses
import subprocess

from datetime import (
    datetime,
    timedelta,
)

from grid import Grid


class Box(object):
    """
    Manages the drawing of boxes.
    """

    def __init__(self, screen, rows, columns, rows_offset=0, columns_offset=0,
                 command=None, interval=None):
        # Set box colors.
        foreground = curses.COLOR_BLACK
        background = curses.COLOR_WHITE
        curses.init_pair(1, foreground, background)

        # Set attributes.
        self.screen = screen
        self.grid = Grid(screen)
        self.rows = rows
        self.columns = columns
        self.rows_offset = rows_offset
        self.columns_offset = columns_offset
        self.command = command
        self.interval = interval

        # Create an empty placeholder box and set it to be refreshed
        # immediately.
        self.box = curses.newpad(1, 1)
        self.next_refresh = datetime.now()

    def refresh(self):
        """
        Re-renders the box.
        """
        # Re-calculate the box's size and position.
        height = self.grid.height(self.rows)
        width = self.grid.width(self.columns)
        x_offset = self.grid.x_offset(self.columns_offset)
        y_offset = self.grid.y_offset(self.rows_offset)

        # Only refresh the contents after waiting for the specified interval.
        if self.next_refresh <= datetime.now():
            self.contents = subprocess.check_output(self.command, shell=True)

            # Calculate the height the pad needs to be to fit the contents.
            lines = self.contents.splitlines()
            if len(lines) >= height:
                # Without adding 1 to height here the program crashes, but I'm
                # not sure why. It doesn't seem like it should be necessary.
                self.pad_height = len(lines) + 1
            else:
                self.pad_height = height

            # Calculate the width the pad needs to be to fit the contents.
            self.pad_width = width
            for line in lines:
                # Add 1 to the string length to allow for end-of-line
                # characters.
                if len(line) >= self.pad_width:
                    self.pad_width = len(line) + 1

            # Set the time of the next refresh.
            self.next_refresh += timedelta(seconds=self.interval)

        # Recreate the box and set its colors.
        self.box = curses.newpad(self.pad_height, self.pad_width)
        self.box.bkgdset(ord(' '), curses.color_pair(1))
        self.box.erase()
        self.box.addstr(self.contents)
        # Subtract 1 from height and width to allow for column and row
        # numbering starting at 0.
        self.box.refresh(
            0,
            0,
            y_offset,
            x_offset,
            y_offset + (height - 1),
            x_offset + (width - 1)
        )
