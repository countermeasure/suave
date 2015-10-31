class Grid(object):
    """
    Provides a responsive grid 12 columns wide and 6 rows high.
    """

    def __init__(self, screen, gutter_width=1):
        self.screen = screen
        self.gutter_width = gutter_width
        self.no_columns = 12
        self.no_rows = 6

    @property
    def column_width(self):
        """Get the column width."""
        screen_width = self.screen.getmaxyx()[1]
        width_of_gutters = self.gutter_width * (self.no_columns + 1)
        return ((screen_width - width_of_gutters) / self.no_columns)

    @property
    def row_height(self):
        """Get the row height."""
        screen_height = self.screen.getmaxyx()[0]
        height_of_gutters = self.gutter_width * (self.no_rows + 1)
        return ((screen_height - height_of_gutters) / self.no_rows)

    def y_offset(self, rows_offset):
        """
        Returns the y-origin point measured in lines.
        """
        row_height_with_gutter = self.row_height + self.gutter_width
        return (self.gutter_width + (row_height_with_gutter * rows_offset))

    def x_offset(self, columns_offset):
        """
        Returns the x-origin point measured in characters.
        """
        col_width_with_gutter = self.column_width + self.gutter_width
        return (self.gutter_width + (col_width_with_gutter * columns_offset))

    def height(self, rows):
        """
        Returns the window height measured in lines.
        """
        return ((self.row_height * rows) + (self.gutter_width * (rows - 1)))

    def width(self, columns):
        """
        Returns the window width measured in characters.
        """
        return (
            (self.column_width * columns) + (self.gutter_width * (columns - 1))
        )
