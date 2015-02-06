from gpiolib import *

import curses

GPIO_PINS = [[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26],
	[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]]

stdscr = None

def setup_curses():
    global stdscr
    stdscr = curses.initscr()
    curses.cbreak()
    stdscr.keypad(1)
    curses.noecho()

def teardown_curses():
    global stdscr
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()


def main():
    global stdscr
    init()
    setup_curses()
    
    try:
	stdscr.addstr(4, 5, "GPIO functions:")
	stdscr.addstr(7, 5, "0: OUT, 1: IN, 40: SERIAL, 41: SPI, 42: I2C, 43: HARD_PWM, -1: UNKNOWN")
	while True:
	    a = []
	    for i, row in enumerate(GPIO_PINS):
		d = []
		for j, cell in enumerate(row):
		    if cell in PINS:
			d.append(get_func(cell))
		    else:
			d.append("x")
		a.append(d)
	    stdscr.addstr(5, 5, str(a[0]))
	    stdscr.addstr(6, 5, str(a[1]))
	    stdscr.refresh()
    except KeyboardInterrupt:
	print "Exiting ..."
    finally:
	teardown_curses()
	cleanup()

if __name__ == "__main__":
    main()
