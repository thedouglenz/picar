from gpiolib import *

def main():
    init()
    set_pin_out(7)
    set_pin_out(26)
    try:
	while True:
	    trigger(7)
	    trigger(26)
    except KeyboardInterrupt:
        print("Exiting and cleaning up...")
    except:
        print("Error halted program. Cleaning up...")
    finally:
        cleanup()
        exit()

if __name__ == "__main__":
    main()
