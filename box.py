import curses


class Box(object):

    def __init__(self, screen, height, width, origin_y=0, origin_x=0,
                 text=None):
        # Set box colors.
        foreground = curses.COLOR_BLACK
        background = curses.COLOR_WHITE
        curses.init_pair(1, foreground, background)

        # Set attributes.
        self.screen = screen
        self.height = height
        self.width = width
        self.origin_y = origin_y
        self.origin_x = origin_x
        self.text = text

        # Create the box and set its colors.
        self.box = curses.newwin(height, width, origin_y, origin_x)
        self.box.bkgdset(ord(' '), curses.color_pair(1))
        self.box.addstr(self.text)

    def refresh(self):
        # Get current screen size.
        screen_width = self.screen.getmaxyx()[1]
        screen_height = self.screen.getmaxyx()[0]
        # Calculate the corner location so the box is centred.
        origin_x = (screen_width - self.width) / 2
        origin_y = (screen_height - self.height) / 2
        # Refresh the box.
        self.box.erase()
        self.box.mvwin(origin_y, origin_x)
        self.box.addstr(self.text)
        self.box.refresh()
