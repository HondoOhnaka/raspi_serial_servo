import sys
from time import sleep
from serial import Serial

START_BYTE = '\xff'

def setup():
    global serialPort
    print "start setup"
    serialPort = Serial("/dev/ttyUSB0", 9600, timeout=2)
    if (serialPort.isOpen() == False):
        try:
            serialPort.open()
        except:
            print "Couldnt' open serial port"
    serialPort.flushInput()
    serialPort.flushOutput()
    print "complete setup"

def set_servo(servo, pos):
    servo_num = servo + 16  # note that the port is always n+16
    s2 = [START_BYTE,  chr(servo_num), chr(pos) ]
    s = '%c%c%c' % (START_BYTE, chr(servo_num), chr(pos))

    serialPort.write(s)
    sleep(.05)
    print 'Moved Servo: %s to pos:%d' % (servo, pos)

def main(args):

    setup()
    print "Completed Setup"

    for i in range(0,255):
    print "Set servo to ", i
    set_servo(0,i)  # only testing a single serv

serialPort.close()

if __name__ == '__main__':
    print "calling  main loop"
    main(sys.argv)
