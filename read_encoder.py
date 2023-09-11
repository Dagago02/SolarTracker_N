import RPi.GPIO as GPIO
from time import sleep

def read_encoder():
    clk = 13
    dt = 11             #Cambiar pines OJOOO!!!!!!!!!!!

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    pot1 = 0
    clkLastState = GPIO.input(clk)

    try:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
            if dtState != clkState:
                pot1 += 1
            else:
                pot1 -= 1
        clkLastState = clkState

    finally:
        print(666)
        GPIO.cleanup()

    return pot1
    
while True:
    
    t=read_encoder()
    print(t)
    sleep(1)
