import datetime
import pvlib
import pandas as pd
import angle_to_voltage as av

def angle_irl(latitud,longitud,zona_horaria,altitud):
	fechahoy = datetime.datetime.now()
	ubicacion = pvlib.location.Location(latitud, longitud)
	
	# Definir la hora y fecha de interes
	#fecha = pd.Timestamp('2023-09-07 14:15:00', tz = zona_horaria)
	fecha = pd.Timestamp(fechahoy, tz = zona_horaria)

	# Obtener la posicion solar
	posicion_solar = pvlib.solarposition.get_solarposition(fecha, ubicacion.latitude, ubicacion.longitude, altitud)

	# Obtener el angulo cenital
	#zenith = float(posicion_solar['apparent_zenith'])
	azimuth = float(posicion_solar['azimuth'])
	elevation = float(posicion_solar['elevation'])

	# Imprimir el resultado
	#print('El angulo cenital es de {} grados.'.format(round(zenith, 2)))
	#print('El angulo azimutal es de {} grados.'.format(round(azimuth, 2)))
	#print('El angulo elevation es de {} grados.'.format(round(elevation, 2)))

	elevation,azimuth = av.angle_to_voltage(elevation,azimuth)
	
	print(elevation)
	print(azimuth)
	return elevation, azimuth

	
		
latitud = 7.1420939356621105
longitud = -73.12132294503459
altitud = 967
zona_horaria = 'Etc/GMT+5'
angle_irl(latitud,longitud,zona_horaria,altitud)
