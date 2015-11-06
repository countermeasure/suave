#!/usr/bin/env python

import curses
import os

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
                rows=box['rows'],
                columns=box['columns'],
                rows_offset=box['rows-offset'],
                columns_offset=box['columns-offset'],
                command=box['command'],
                interval=box['interval'],

            )
        )

    while True:
        # Redraw the screen only when it changes.
        if screen.is_wintouched():
            screen.clear()
            screen.refresh()

        # Give every box an opportunity to redraw if it has changed.
        [box.redraw_if_changed() for box in boxes]

        # Wait before redrawing again.
        curses.napms(1000)


curses.wrapper(main)
