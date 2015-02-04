import RPi.GPIO as gpio

GND = 6
PINS = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26]

def init():
    gpio.setmode(gpio.BOARD)
    for i in PINS:
	if gpio.gpio_function(i) == gpio.OUT:
	    gpio.cleanup()
	    break

def set_pin_out(pin):
    if pin in PINS:
        gpio.setup(pin, gpio.OUT)

def set_pin_in(pin):
    if pin in PINS:
	gpio.setup(pin, gpio.IN)

def cleanup():
    gpio.cleanup()

def trigger(pin):
    gpio.output(pin, gpio.HIGH)


