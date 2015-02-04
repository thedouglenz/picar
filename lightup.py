from gpiolib import *

def main():
    init()
    set_pin_out(7)
    while True:
	try:
	    trigger(7)
	except KeyboardInterrupt:
	    cleanup()
	    exit()

if __name__ == "__main__":
    main()
