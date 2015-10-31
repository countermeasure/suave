class Grid(object):
    """
    Provides a responsive grid 12 columns wide and 6 rows high.
    """

    def __init__(self, screen, gutter_width=1):
        self.no_columns = 12
        self.no_rows = 6
        self.screen = screen
        self.gutter_width = gutter_width

        screen_width = screen.getmaxyx()[1]
        screen_height = screen.getmaxyx()[0]

        self.column_width = (
            (screen_width - (gutter_width * (self.no_columns + 1))) / 12
        )
        self.row_height = (
            (screen_height - (gutter_width * (self.no_rows + 1))) / 6
        )

    def y_offset(self, rows_offset):
        """
        Returns the y-origin point measured in lines.
        """
        return (
            self.gutter_width + (
                (self.row_height + self.gutter_width) * rows_offset
            )
        )

    def x_offset(self, columns_offset):
        """
        Returns the x-origin point measured in characters.
        """
        return (
            self.gutter_width + (
                (self.column_width + self.gutter_width) * columns_offset
            )
        )

    def height(self, rows):
        """
        Returns the height point measured in lines.
        """
        return ((self.row_height * rows) + (self.gutter_width * (rows - 1)))

    def width(self, columns):
        """
        Returns the width point measured in characters.
        """
        return (
            (self.column_width * columns) + (self.gutter_width * (columns - 1))
        )

    def refresh(self):
        """
        Refreshes the column widths and row heights.
        """
        screen_width = self.screen.getmaxyx()[1]
        screen_height = self.screen.getmaxyx()[0]

        self.column_width = (
            (screen_width - (self.gutter_width * (self.no_columns + 1))) / 12
        )
        self.row_height = (
            (screen_height - (self.gutter_width * (self.no_rows + 1))) / 6
        )
