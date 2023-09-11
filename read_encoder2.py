import RPi.GPIO as GPIO
from time import sleep

def read_encoder2():
    clk2 = 0
    dt2 = 0             #Cambiar pines OJOOO!!!!!!!!!!!

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(clk2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(dt2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    pot2 = 0
    clkLastState2 = GPIO.input(clk2)

    try:
        clkState2 = GPIO.input(clk2)
        dtState2 = GPIO.input(dt2)
        if clkState2 != clkLastState2:
            if dtState2 != clkState2:
                pot2 += 1
            else:
                pot2 -= 1
        clkLastState2 = clkState2

    finally:
        GPIO.cleanup()

    return pot2