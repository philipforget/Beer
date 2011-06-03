#!/usr/bin/python
from serial import Serial
from datetime import datetime
import time

class Main():
    def __init__(self):
        self.tty      = "/dev/ttyUSB0"
        self.baud     = 9600
        self.log_name = "temp.log"

    def run(self):
        ser = Serial(self.tty, self.baud)
        with open(self.log_name, 'wa') as log_file:
            while True:
                line = ser.readline()
                try:
                    cel = float(line)
                except ValueError:
                    continue

                far = c_to_f(cel)
                print("%s, %d" % (datetime.now(), far))
                time.sleep(1)


def c_to_f(far):
    return  (far * (9.0/5.0)) + 32


if __name__ == '__main__':
    main = Main()
    main.run()
