from gpiolib import *

PINOUT = 7

K_UP = 38

def startup():
    init()
    set_pin_out(PINOUT)
    send_low(PINOUT)

def key_in(keys):
    if K_UP in keys:
        trigger(PINOUT)

def key_release(key):
    if not K_UP in keys:
        send_low(PINOUT)
