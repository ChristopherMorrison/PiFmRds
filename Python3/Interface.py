#imports
import locale
import sys
from dialog import Dialog


def main():
    # set locale for the program
    locale.setlocale(locale.LC_ALL, '')

    # Setup the dialog object
    d = Dialog(dialog="dialog")
    d.set_background_title("Python FM Radio Data System")

    while(1):
        # print menu
        dcode, tag = d.menu("Select an option:",
                   choices=[("Frequency", "Set the broadcast frequency."),
                            ("Audio", "Choose the audio source to play."),
                            ("PI", "???"),
                            ("PS","Set the station name."),
                            ("RT","Set the radiotext."),
                            ("CTL","???Pipe name use"),
                            ("PPM","Set the oscillation error in ppm.")])

        print(dcode)
        print(tag)
        # evaluate
    
    sys.exit()
if __name__ == "__main__":
    main()
