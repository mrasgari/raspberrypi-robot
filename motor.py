import RPi.GPIO as GPIO
from time import sleep
import curses

in1 = 24
in2 = 23
in3 = 16
in4 = 20
en = 25
en2 = 21
temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
p = GPIO.PWM(en, 1000)
p2 = GPIO.PWM(en2, 1000)
p.start(25)
p2.start(25)

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)

try:
    while True:
        char = screen.getch()

        if char == ord('q'):
            break
        elif char == curses.KEY_RIGHT:
            print("right")
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in4, GPIO.HIGH)
            GPIO.output(in3, GPIO.LOW)
        elif char == curses.KEY_LEFT:
            print("left")
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in4, GPIO.LOW)
            GPIO.output(in3, GPIO.HIGH)
        elif char == curses.KEY_UP:
            print("forward")
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            GPIO.output(in3, GPIO.LOW)
        elif char == curses.KEY_DOWN:
            print('back')
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
        elif char == ord('s'):
            print("high")
            p.ChangeDutyCycle(100)
            p2.ChangeDutyCycle(100)
        elif char == curses.KEY_BACKSPACE:
            print("stop")
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.LOW)
finally:
    # shut down cleanly
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
    GPIO.cleanup()
