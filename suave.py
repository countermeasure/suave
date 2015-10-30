#!/usr/bin/env python

import curses
import os
import time

from box import Box
from utils import load_yaml


def main(screen):
    """
    Draws and redraws the screen.
    """
    # Hide the cursor.
    curses.curs_set(0)

    # Load config from file.
    config = load_yaml(os.path.expanduser('~/.suave/config.yml'))

    # Create boxes from config.
    boxes = []
    for box in config:
        boxes.append(
            Box(
                screen=screen,
                height=box['height'],
                width=box['width'],
                origin_y=box['y-origin'],
                origin_x=box['x-origin'],
                command=box['command'],
                interval=box['interval'],

            )
        )

    while True:
        # Re/draw the screen and boxes.
        screen.erase()
        screen.refresh()
        [box.refresh() for box in boxes]

        # Wait before redrawing again.
        time.sleep(1)


curses.wrapper(main)
