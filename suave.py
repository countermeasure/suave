#!/usr/bin/env python

import curses
import time

from box import Box


def main(screen):
    """
    Draws and redraws the screen.
    """
    # Hide the cursor.
    curses.curs_set(0)

    box1 = Box(
        screen=screen,
        height=2,
        width=3,
        text='\n   Top left box.',
    )

    box2 = Box(
        screen=screen,
        height=2,
        width=3,
        origin_y=4,
        origin_x=9,
        text='\n   Bottom right box.',
    )

    while True:
        # Re/draw the screen and box.
        screen.erase()
        screen.refresh()
        box1.refresh()
        box2.refresh()

        # Wait before redrawing again.
        time.sleep(1)


curses.wrapper(main)
