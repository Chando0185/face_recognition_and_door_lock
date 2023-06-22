from pyfirmata import Arduino, SERVO

PORT="COM7"

pin=10

board=Arduino(PORT)

board.digital[pin].mode=SERVO

def rotateServo(pin, angle):
    board.digital[pin].write(angle)

def doorAutomate(val):
    if val==0:
        rotateServo(pin, 220)
    elif val==1:
        rotateServo(pin, 40)