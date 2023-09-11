import RPi.GPIO as GPIO
from time import sleep
import serial
from angle_to_voltage import angle_to_voltage
import angle_irl as ag
import comparador as cp
#import Pruebas2 as prx
import pandas as pd
import pvlib
import datetime
import numpy as np
#import read_encoder as rc
#import read_encoder2 as rc2
import threading

#GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
################codigo prueba lectura pot################################################
# Pines para el primer potenciómetro
clk1 = 13
dt1 = 11

# Pines para el segundo potenciómetro
clk2 = 15
dt2 = 16

# Variables para almacenar los estados anteriores de los potenciómetros
pot1 = 0
pot2 = 0
archivo = open("Potenciometros.txt", "r")
for linea in archivo.readlines():
    columna= str(linea).split(",")
    pot1=int(columna[0])
    pot2=int(columna[1])
    #print(columna[0])
    #print(columna[1])
################################################################



clkLastState1 = GPIO.LOW
clkLastState2 = GPIO.LOW

GPIO.setmode(GPIO.BOARD)

# Configurar los pines para el primer potenciómetro
GPIO.setup(clk1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Configurar los pines para el segundo potenciómetro
GPIO.setup(clk2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def read_potenciometro1():
    global pot1, clkLastState1

    while True:
        clkState1 = GPIO.input(clk1)
        dtState1 = GPIO.input(dt1)
        if clkState1 != clkLastState1:
            if dtState1 != clkState1:
                pot1 += 1
            else:
                pot1 -= 1
            #print("Potenciómetro 1:", pot1)
        clkLastState1 = clkState1
        sleep(0.01)

def read_potenciometro2():
    global pot2, clkLastState2

    while True:
        clkState2 = GPIO.input(clk2)
        dtState2 = GPIO.input(dt2)
        if clkState2 != clkLastState2:
            if dtState2 != clkState2:
                pot2 += 1
            else:
                pot2 -= 1
            #print("Potenciómetro 2:", pot2)
        clkLastState2 = clkState2
        sleep(0.01)

def obtener_valor_contador1():
    global pot1
    return pot1

def obtener_valor_contador2():
    global pot2
    return pot2
#fin codigo prueba



latitud = 7.1420939356621105
longitud = -73.12132294503459
altitud = 967
zona_horaria = 'Etc/GMT+5'
GPIO.setmode(GPIO.BOARD)
MIN1=29
MIN2=31         #poner pines OJO !!!!!!!!!!!!!!!!!!!!!!!!!!
MIN3=33
MIN4=35
#prueba=37
GPIO.setup(MIN1, GPIO.OUT)
GPIO.setup(MIN2, GPIO.OUT)
GPIO.setup(MIN3, GPIO.OUT)
GPIO.setup(MIN4, GPIO.OUT)
#GPIO.setup(prueba, GPIO.OUT)

#codigo prueba bucle
try:
	# Crear hilos para ejecutar los bucles de lectura de los potenciómetros
	t1 = threading.Thread(target=read_potenciometro1)
	t1.start()

	t2 = threading.Thread(target=read_potenciometro2)
	t2.start()
    # Lógica principal del programa
	while True:
		elevacion,azimuth = ag.angle_irl(latitud,longitud,zona_horaria,altitud)
		pot1 = obtener_valor_contador1()
		print(pot1)
		pot2 = obtener_valor_contador2()
		print(pot2)
		print(elevacion)
		print(azimuth)
        ##################################################################################################nuevo##########################################
		archivo= open("Potenciometros.txt","w") 
		archivo.write(f"{pot1},{pot2}")
		##################################################################################################nuevo##########################################
		#print("Valor del potenciómetro 1:", pot1)
		#print("Valor del potenciómetro 2:", pot2)
		# Resto de la lógica de tu programa...
		IN1, IN2, IN3, IN4 = cp.comparador(pot1, pot2, azimuth, elevacion)

		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(MIN1, GPIO.OUT)
		GPIO.setup(MIN2, GPIO.OUT)
		GPIO.setup(MIN3, GPIO.OUT)
		GPIO.setup(MIN4, GPIO.OUT)
		#GPIO.setup(prueba, GPIO.OUT)
		#GPIO.output(prueba, GPIO.HIGH)
		if IN1 == 1:
			GPIO.output(MIN1, GPIO.HIGH)
		elif IN1 == 0:
			GPIO.output(MIN1, GPIO.LOW)
		if IN2 == 1:
			GPIO.output(MIN2, GPIO.HIGH)
		elif IN2 == 0:
			GPIO.output(MIN2, GPIO.LOW)
		if IN3 == 1:
			GPIO.output(MIN3, GPIO.HIGH)
		elif IN3 == 0:
			GPIO.output(MIN3, GPIO.LOW)
		if IN4 == 1:
			GPIO.output(MIN4, GPIO.HIGH)
		elif IN4 == 0:
			GPIO.output(MIN4, GPIO.LOW)
		sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
#fin codigo prueba bucle
