from gpiolib import *
from time import sleep

import curses

SLEEP = 0.25
P = [7, 26, 10]

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
    for i in P:
	set_pin_out(i)
	send_low(i)
    try:
	stdscr.addstr(4, 5, "Light on: ")
	while True:
	    for k, i in enumerate(P):
		a = [0, 0, 0]
		trigger(i)
		a[k] = 1
		stdscr.addstr(5, 5, str(a))
		stdscr.refresh()
		sleep(SLEEP)
		send_low(i)
    except KeyboardInterrupt:
        print("Exiting and cleaning up...")
    except:
        print("Error halted program. Cleaning up...")
    finally:
        cleanup()
	teardown_curses()
        exit()

if __name__ == "__main__":
    main()
