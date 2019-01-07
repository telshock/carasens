import epd2in13b

class Display(epd2in13b.EPD):
    """
    Extends the manufacturer's display class to provide additional functionality.

    This Display class is aware of how long it takes to update the screen and has an
    is_ready method to show when it is done updating.
    """
    def __init__(self):
        self.init()
        self.set_rotate(3)
        self.ready = True

    def is_ready(self):
        """
        Check if the display is ready to draw a new frame.

        :return: True/False
        """
        return self.digital_read(self.busy_pin)

    def display_frame(self, black, red):
        """
        Draw the red and black frames to the display.

        Extend the manufacturer's method so that it spawns in a thread. We want to be able to still get the ready status
        while this display updates.

        :param black: The black frame.
        :param red: The red frame.
        :return:
        """
        if self.is_ready() is True:
            # spawn super in thread
        else:
            # raise DisplayBusyException


