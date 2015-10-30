#!/usr/bin/env python

import curses
import time

from box import Box


def main(screen):
    # Hide the cursor.
    curses.curs_set(0)

    # Create the box.
    width = 40
    height = 9
    text_padding = '%s' % ('\n' * (height / 2))
    text_body = '{:^{width}}'.format(
        'This is how SUAVE begins.',
        width=width
    )
    box = Box(
        screen=screen,
        height=height,
        width=width,
        text='%s%s' % (text_padding, text_body)
    )

    while True:
        # Re/draw the screen and box.
        screen.erase()
        screen.refresh()
        box.refresh()

        # Wait before redrawing again.
        time.sleep(1)


curses.wrapper(main)
