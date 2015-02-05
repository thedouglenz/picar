""" This program exhibits using the curses module and turning on and off an LED by keyboard events
    Douglas Lenz
"""
from gpiolib import *

import curses

OUTPIN = 7

stdscr = None

def setup_pins():
    init()
    set_pin_out(OUTPIN)

def init_screen():
    global stdscr
    print "Starting curses ..."
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)

def getchar():
    global stdscr
    key = ''
    key = stdscr.getch()
    return key

def main():
    global stdscr
    setup_pins()
    init_screen()
    print "Press w to turn on the light"

    try:
	while True:
	    on = is_on(OUTPIN)
	    if(on):
		stdscr.addstr(20, 20, "Light is ON")
	    else:
		stdscr.addstr(20, 20, "Light is OFF")
	    stdscr.refresh()

	    c = getchar()

	    if c == ord('q'): # pressing q will exit
		break
	    if c == curses.KEY_UP: # KEY_UP should turn the light on
		trigger(OUTPIN)
	    if c == curses.KEY_DOWN:
		send_low(OUTPIN)

    except KeyboardInterrupt:
	print "Exiting..."
    finally:
	curses.endwin()
	cleanup()

if __name__ == "__main__":
    main()
