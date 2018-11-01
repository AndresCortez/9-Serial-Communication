#!/usr/bin/python

import sys
import time
import difflib
import pigpio
RX=15




try:
	pi = pigpio.pi()
	#pi.set_mode(TX, pigpio.OUTPUT)
	pi.set_mode(RX, pigpio.INPUT)
	#pi.wave_clear()	#Se elimina cualquier dato que exista en el buffer
	#pi.wave_add_serial(TX,9600,'\x01',0,8)	# Se crea la onda con 1 bit de start y 1 de stop
	#wid = pi.wave_create()	# Devuelve el id de la onda creada
	pi.bb_serial_read_open(RX, 9600,9)
	print "DATA - SOFTWARE SERIAL:"
	
	#pi.wave_clear()
	#pi.wave_delete(wid)	#Elimina la onda con el dato existente
	#while pi.wave_tx_busy():	#Mientras no se haya enviado todos los datos se quedara en el loop
	#	pass
	while 1:
		(count, data) = pi.bb_serial_read(RX)
		if count:
			print data
			print hex(ord(data))
		time.sleep(1)
		#pi.wave_send_once(wid)	#Envia la onda con los datos ya creados 
except:
	pi.bb_serial_read_close(RX)
	print("Hubo un error en la conexion")
	pi.stop()

