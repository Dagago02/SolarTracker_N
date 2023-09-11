from RPi import GPIO
import threading
from time import sleep

clk = 13
dt = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pot1 = 0
clkLastState = GPIO.input(clk)

def read_potenciometro():
    global pot1, clkLastState

    while True:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
            if dtState != clkState:
                pot1 += 1
            else:
                pot1 -= 1
            print(pot1)
            #clkLastState = clkState
        clkLastState = clkState
        sleep(0.01)

def obtener_valor_contador():
    global pot1
    return pot1

try:
    # Crear un hilo para ejecutar el bucle de lectura del potenciómetro
    t = threading.Thread(target=read_potenciometro)
    t.start()

    # Lógica principal del programa
    while True:
        valor = obtener_valor_contador()
        print(f"Valor del contador: {valor}")
        sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
