from gpiolib import *

def main():
    init()
    set_pin_out(7)
    try:
	while True:
	    trigger(7)
    except KeyboardInterrupt:
        print("Exiting and cleaning up...")
    except:
        print("Error halted program. Cleaning up...")
    finally:
        cleanup()
        exit()

if __name__ == "__main__":
    main()
