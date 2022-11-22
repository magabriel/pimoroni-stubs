from picographics import PicoGraphics


# ----------------------------------------
# Galactic Unicorn
# ----------------------------------------


class GalacticUnicorn:
    """
    The Galactic Unicorn library provides a collection of methods that allow you to easily access all of the features on the board.
    """

    WIDTH = 53
    HEIGHT = 11

    SWITCH_A = 0
    SWITCH_B = 1
    SWITCH_C = 3
    SWITCH_D = 6
    SWITCH_SLEEP = 27
    SWITCH_VOLUME_UP = 7
    SWITCH_VOLUME_DOWN = 8
    SWITCH_BRIGHTNESS_UP = 21
    SWITCH_BRIGHTNESS_DOWN = 26

    # ----------------------------------------
    # System State
    # ----------------------------------------

    def set_brightness(self, value: float) -> None:
        """
        Set the brightness - value is supplied as a floating point value between 0.0 and 1.0.
        """

    def is_pressed(self, button: int) -> None:
        """
        Returns true if the requested button is currently pressed.

        There are a set of constants in the GalacticUnicorn class that represent each of the buttons.

        The brightness, sleep, and volume buttons are not tied to hardware functions (they are implemented entirely in software) so can also be used for user functions if preferred.

        Here's a list of the constants and their associated pin numbers:

        - SWITCH_A = 0
        - SWITCH_B = 1
        - SWITCH_C = 3
        - SWITCH_D = 6
        - SWITCH_SLEEP = 27
        - SWITCH_VOLUME_UP = 7
        - SWITCH_VOLUME_DOWN = 8
        - SWITCH_BRIGHTNESS_UP = 21
        - SWITCH_BRIGHTNESS_DOWN = 26
        """

    def get_brightness(self) -> float:
        """
        Returns the current brightness as a value between 0.0 and 1.0.
        """

    def adjust_brightness(self, delta: float) -> None:
        """
        Adjust the brightness of the display - delta is supplied as a floating point value and will be added to the current brightness (and then clamped to the range 0.0 to 1.0).

        For example:

        - gu.set_brightness(0.5)
        - gu.adjust_brightness(0.1)  # brightness is now 0.6
        - gu.adjust_brightness(0.7)  # brightness is now 1.0
        - gu.adjust_brightness(-0.2)  # brightness is now 0.8
        """

    def set_volume(self, value: float) -> None:
        """
        Set the volume - value is supplied as a floating point value between 0.0 and 1.0.
        """

    def get_volume(self) -> float:
        """
        Returns the current volume as a value between 0.0 and 1.0.
        """

    def adjust_volume(self, delta: float) -> None:
        """
        Adjust the volume - delta is supplied as a floating point value and will be added to the current volume (and then clamped to the range 0.0 to 1.0).

        For example:

        - gu.set_volume(0.5)
        - gu.set_volume(0.1)  # volume is now 0.6
        - gu.adjust_volume(0.7)  # volume is now 1.0
        - gu.adjust_volume(-0.2)  # volume is now 0.8
        """

    def light(self) -> None:
        """
        Get the current value seen by the onboard light sensor as a value between 0 and 4095.
        """

    # ----------------------------------------
    # Drawing
    # ----------------------------------------

    def update(self, graphics: PicoGraphics) -> None:
        """
        The PicoGraphics library provides a collection of powerful drawing methods to make things simple.

        The image on the PicoGraphics object provided is copied to the interleaved framebuffer with gamma correction applied.

        For example (assuming you've set up your Galactic Unicorn and PicoGraphics objects up as we did above):

        gu.update(graphics)

        warning If you've used PicoGraphics on our other boards note that this update function works a little differently. Here it's a Galactic Unicorn function to which you need to pass a PicoGraphics object to.
        """

    def clear(self) -> None:
        """
        Clear the contents of the interleaved framebuffer.

        This will make your Galactic Unicorn display turn off.

        To show an image again, call the update() function as described above.
        """

    # ----------------------------------------
    # Audio
    # ----------------------------------------

    def play_sample(self, data: bytearray) -> Channel:
        """
        Play the provided 16-bit audio sample. data must point to a bytearray that contains 16-bit PCM data. The number of samples is retrieved from the array's length.
        """

    def synth_channel(self, channel: int) -> Channel:
        """
        Gets a Channel object which can then be configured with voice, ADSR envelope, etc.
        """

    def play_synth(self):
        """
        Start the synth playing.
        """

    def stop_playing(self):
        """
        Stops any currently playing audio.
        """


# ----------------------------------------
# Channel
# ----------------------------------------


class Channel:

    TRIANGLE = 0
    """ Fake value"""
    SQUARE = 0
    """ Fake value"""
    SINE = 0
    """ Fake value"""
    NOISE = 0
    """ Fake value"""

    def configure(self,
                  waveforms: float | None = None,
                  frequency: float | None = None,
                  volume: float | None = None,
                  attack: float | None = None,
                  decay: float | None = None,
                  sustain: float | None = None,
                  release: float | None = None,
                  pulse_width: float | None = None) -> None:
        """ """

    def restore(self) -> None:
        """ """

    def waveforms(self, waveforms: float | None = None) -> float | None:
        """ """

    def frequency(self, frequency: float | None = None) -> float | None:
        """ """

    def volume(self, volume: float | None = None) -> float | None:
        """ """

    def attack_duration(self, duratio: float | None = None) -> float | None:
        """ """

    def decay_duration(self, duration: float | None = None) -> float | None:
        """ """

    def sustain_level(self, level: float | None = None) -> float | None:
        """ """

    def release_duration(self, duration: float | None = None) -> float | None:
        """ """

    def pulse_width(self, width: float | None = None) -> float | None:
        """ """

    def trigger_attack(self):
        """ Start the channel playing """

    def trigger_release(self):
        """ Stop the channel playing """

    def play_tone(self, frequency: int, volume: float | None = None, attack: float | None = None, release: float | None = None):
        """ """
