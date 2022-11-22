from typing import List, Tuple

# ----------------------------------------
# Picographics
# ----------------------------------------


class PicoGraphics:

    def __init__(self, display, pen_type=PEN_RGB332, rotate=0):
        """
        All SPI LCDs support 0, 90, 180 and 270 degree rotations.
        """

    def create_pen(self, r: int, g: int, b: int) -> int:
        """ 
        Create a pen colour for drawing into a screen (for RGB888, RGB565, RGB332, P8 and P4 modes).

        In RGB565 and RGB332 modes this packs the given RGB into an integer representing a colour in these formats and returns the result.

        In P4 and P8 modes this will consume one palette entry, or return an error if your palette is full. Palette colours are stored as RGB and converted when they are displayed on screen.
        """

    def set_pen(self, my_pen: int):
        """ 
        Tell PicoGraphics which pen to use.

        For RGB888, RGB565, RGB332, P8 and P4 modes):

        - This will be either an RGB332, RGB565 or RGB888 colour, or a palette index.

        For 1BIT mode - such as for Inky Pack and the Mono OLED - pens are handled a little differently:

        - There's no need to create one, since mapping an RGB colour to black/white is meaningless.
        - Instead you can pick from 16 shades of grey which are automatically dithered into the PicoGraphics buffer, where:

                - 0 is Black,
            - 1 - 14 are shades of grey,
            - 15 is white.

        Inky Frame:

            Inky Frame is a special case- the display itself supports only 7 (8 if you include its cleaning "clear" colour, which we call Taupe) colours.

                - BLACK = 0
                - WHITE = 1
                - GREEN = 2
                - BLUE = 3
                - RED = 4
                - YELLOW = 5
                - ORANGE = 6
                - TAUPE = 7
       """

    def set_backlight(self, brightness: float):
        """
        Control The Backlight

        You can set the display backlight brightness between 0.0 and 1.0.
        """

    def set_clip(self, x: int, y: int, w: int, h: int):
        """
        Set the clipping bounds for drawing.
        """

    def remove_clip(self):
        """
        Remove the clipping bounds.
        """

    def clear(self):
        """
        Clear the display to the current pen colour.

        This is equivalent to:

        w, h = display.get_bounds()
        display.rectangle(0, 0, w, h)

        You can clear portions of the screen with rectangles to save time redrawing things like JPEGs or complex graphics.
        """

    def update(self):
        """
        Send the contents of your Pico Graphics buffer to your screen.

        If you are using a Galactic Unicorn, then the process for updating the display is different. Instead of the above, do:

        galactic_unicorn.update(display)
        """

    # ----------------------------------------
    # Text
    # ----------------------------------------

    def set_font(self, font: str):
        """Change the font.

       - Bitmap fonts. These are aligned from their top-left corner.
                - 'bitmap6'
                - 'bitmap8'
                - 'bitmap14_outline'

        - Vector(Hershey) fonts. These are aligned to their midline.
                - 'sans'
                - 'gothic'
                - 'cursive'
                - 'serif_italic'
                - 'serif'
        """

    def text(self, text: str, x: int, y: int, wordwrap: int, scale: int | float, angle: int = 0, spacing: int = 0):
        """
        Write some text:

            - text - the text string to draw
            - x - the destination X coordinate
            - y - the destination Y coordinate
            - wordwrap - number of pixels width before trying to break text into multiple lines
            - scale - size
            - angle - rotation angle(Vector only!)
            - spacing - letter spacing

        Text scale can be a whole number(integer) for Bitmap fonts, or a decimal(float) for Vector(Hershey) fonts.

        For example:

            display.set_font("bitmap8")

            display.text("Hello World", 0, 0, scale=2)

            Draws "Hello World" in a 16px tall, 2x scaled version of the bitmap8 font.
        """

    def measure_text(self, text: str, scale: int | float = 1, spacing: int = 0) -> int | float:
        """
        Measure a text string for centering or alignment on screen.

        The height of each Bitmap font is explicit in its name.
        """

    def character(self, char: str, x: int, y: int, scale: int | float = 1):
        """
        Write a single character.
        """

    # ----------------------------------------
    # Basic Shapes
    # ----------------------------------------

    def line(self, x1: int, y1: int, x2: int, y2: int):
        """
        Draw a line.

        The X1/Y1 and X2/Y2 coordinates describe the start and end of the line respectively.
        """

    def circle(self, x: int, y: int, r: int):
        """
        Draw a circle.

        - x - the destination X coordinate
        - y - the destination Y coordinate
        - r - the radius

        The X/Y coordinates describe the center of your circle.
        """

    def rectangle(self, x: int, y: int, w: int, h: int):
        """
        Draw a rectangle.

        Rectangle
        - x - the destination X coordinate
        - y - the destination Y coordinate
        - w - the width
        - h - the eight
        """

    def triangle(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
        """ 
        Draw a triangle.

        The three pairs of X/Y coordinates describe each point of the triangle.
        """

    def polygon(self, points: List[Tuple[int, int]]):
        """
        Draw a polygon.

        To draw other shapes, you can provide a list of points (x, y) to polygon.
        """

    # ----------------------------------------
    # Pixels
    # ----------------------------------------

    def pixel(self, x: int, y: int, length=1):
        """
        Set an individual pixel.
        """

    def pixel_span(self, x: int, y: int, length=1):
        """
        Set a horizontal span of pixels. 
        """

    # ----------------------------------------
    # Palette Management
    # ----------------------------------------

    def set_palette(self, palette: List[Tuple[int, int, int]]):
        """
        Set n elements in the palette from a list of RGB tuples:

        set_palette([(r, g, b),(r, g, b),(r, g, b)])

        Intended for P4 and P8 modes.

        You have a 16-color and 256-color palette respectively.
        """

    def update_pen(self, index: int, r: int, g: int, b: int):
        """
        Update an entry in the P4 or P8 palette with the given colour.

        This is stored internally as RGB and converted to whatever format your screen requires when displayed.
        """

    def reset_pen(self, index: int):
        """
        Reset a pen back to its default value(black, marked unused).
        """

    # ----------------------------------------
    # Utility Functions
    # ----------------------------------------

    def RGB332_to_RGB(self):
        """TODO"""

    def RGB_to_RGB332(self):
        """TODO"""

    def RGB565_to_RGB(self):
        """TODO"""

    def RGB_to_RGB565(self):
        """TODO"""

    # ----------------------------------------
    # Sprites
    # ----------------------------------------

    def load_spritesheet(self, file_name: str):
        """ 
        Load a spritesheet.

        Pico Display has very limited support for sprites in RGB332 mode.

        You'll need to include the pen_type in the import statement, and define the pen_type before using loading the spritesheet:

        - from picographics import PicoGraphics, PEN_RGB565, PEN_RGB332
        - display = PicoGraphics(display=PICO_DISPLAY, pen_type=PEN_RGB332)
        - display.load_spritesheet("s4m_ur4i-dingbads.rgb332")
        - display.update()
        - display.sprite(0, 0, 0, 0)

        Sprites must be 8x8 pixels arranged in a 128x128 pixel spritesheet. 
        1-bit transparency is handled by electing a single colour to skip over.
        """

    def sprite(self, sprite_x: int, spryte_y: int, dest_x: int, dest_y: int, scale: int = 1, transparent: int = 0):
        """
        Display a sprite.

            - sprite_x: Sprite X position(from 0-15) - this selects the horizontal location of an 8x8 sprite from your 128x128 pixel spritesheet.
            - sprite_y: Sprite Y position(from 0-15)
            - dest_x: Destination X - where to draw on your screen horizontally
            - dest_y: Destination Y = where to draw on your screen vertically
            - scale(optional) - an integer scale value, 1 = 8x8, 2 = 16x16 etc.
            - transparent(optional) - specify a colour to treat as transparent
        """


# ----------------------------------------
# Supported Displays
# ----------------------------------------

DISPLAY_PICO_DISPLAY = 0
"""
Pico Display - 240x135 SPI LCD
    - Fake value
"""

DISPLAY_PICO_DISPLAY_2 = 0
"""
Pico Display 2 - 320x240 SPI LCD
    - Fake value
"""

DISPLAY_TUFTY_2040 = 0
"""
Tufty 2040 - 320x240 Parallel LCD
    - Fake value
"""

DISPLAY_PICO_EXPLORER = 0
"""
Pico Explorer - 240x240 SPI LCD
    - Fake value
"""

DISPLAY_ENVIRO_PLUS = 0
"""
Enviro Plus - 240x240 SPI LCD
    - Fake value
"""

DISPLAY_ROUND_LCD_240X240 = 0
"""
240x240 Round SPI LCD Breakout
    - Fake value
"""

DISPLAY_LCD_240X240 = 0
"""
240x240 Square SPI LCD Breakout
    - Fake value
"""

DISPLAY_LCD_160X80 = 0
"""
160x80 SPI LCD Breakout
    - Fake value
"""

DISPLAY_I2C_OLED_128X128 = 0
"""
128x128 I2C OLED
    - Fake value
"""

DISPLAY_INKY_PACK = 0
"""
Pico Inky Pack - 296x128 mono e-ink
    - Fake value
"""

DISPLAY_INKY_FRAME = 0
"""
Inky Frame - 600x447 7-colour e-ink
    - Fake value
"""

DISPLAY_GFX_PACK = 0
"""
Pico GFX Pack - 128x64 mono LCD Matrix
    - Fake value
"""

DISPLAY_GALACTIC_UNICORN = 0
"""
Galactic Unicorn - 53x11 LED Matrix
    - Fake value
"""

# ----------------------------------------
# Supported Graphics Modes(Pen Type)
# ----------------------------------------

PEN_1BIT = 0
"""
1-bit - mono, used for Pico Inky Pack and i2c OLED
    - Fake value
"""

PEN_3BIT = 0
"""
3-bit - 8-colour, used for Inky Frame
    - Fake value
"""

PEN_P4 = 0
"""
4-bit - 16-colour palette of your choice
    - Fake value
"""

PEN_P8 = 0
"""
8-bit - 256-colour palette of your choice
    - Fake value
"""

PEN_RGB332 = 0
"""
8-bit RGB332 - 256 fixed colours(3 bits red, 3 bits green, 2 bits blue)
    - Fake value
"""

PEN_RGB565 = 0
"""
16-bit RGB565 - 64K colours at the cost of RAM. (5 bits red, 6 bits green, 5 bits blue)
    - Fake value
"""

PEN_RGB888 = 0
"""
24-bit RGB888 - 16M colours at the cost of lots of RAM. (8 bits red, 8 bits green, 8 bits blue)
    - Fake value
"""
