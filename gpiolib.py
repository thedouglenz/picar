""" A library that abstracts away the common functions in RPi.GPIO
    that are necessary to interface with the GPIO pins
"""
import RPi.GPIO as gpio

GND = 6
PINS = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26]
REFMODE = gpio.BOARD # can be BOARD or BCM

def init():
    """Prepare the GPIO pins by setting the mode they will be referenced
    and running cleanup"""
    gpio.setmode(REFMODE)
    for i in PINS:
	if gpio.gpio_function(i) == gpio.OUT:
	    gpio.cleanup()
	    break

def set_pin_out(pin):
    """Setup a pin as an output pin only if it is a touchable pin"""
    if pin in PINS:
        gpio.setup(pin, gpio.OUT)

def set_pin_in(pin):
    """Setup a pin as an input pin only if it is a touchable pin"""
    if pin in PINS:
	gpio.setup(pin, gpio.IN)

def cleanup():
    """De-assign functions to all the pins"""
    gpio.cleanup()

def trigger(pins):
    """Send a +3V signal across the given pin"""
    gpio.output(pins, gpio.HIGH)


