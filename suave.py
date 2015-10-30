#!/usr/bin/env python

import curses
import time


def main(screen):
    # Hide the cursor.
    curses.curs_set(0)

    # Set panel colors.
    foreground = curses.COLOR_BLACK
    background = curses.COLOR_WHITE
    curses.init_pair(1, foreground, background)

    while True:
        # Get current screen size.
        screen_width = screen.getmaxyx()[1]
        screen_height = screen.getmaxyx()[0]

        # Set panel size, location and colors.
        height = 9
        width = 40
        origin_x = (screen_width - width) / 2
        origin_y = (screen_height - height) / 2
        panel = curses.newwin(height, width, origin_y, origin_x)
        panel.bkgdset(ord(' '), curses.color_pair(1))

        # Re/draw the screen and panel, centering text horizontally and
        # vertically in the panel.
        screen.erase()
        panel.erase()
        panel.addstr('%s' % ('\n' * (height / 2)))
        panel.addstr('{:^{width}}'.format(
            'This is how SUAVE begins.',
            width=width)
        )
        screen.refresh()
        panel.refresh()

        # Wait before redrawing again.
        time.sleep(1)


curses.wrapper(main)
