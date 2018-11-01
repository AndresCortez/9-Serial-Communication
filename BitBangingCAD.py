#!/usr/bin/python
import sys
import time
import difflib
import pigpio

MDB_ACK  = 0x000
MDB_RST  = 0x110
MDB_STP  = 0x111
MDB_POLL = 0x112
MDB_VEND = 0x113
MDB_READ = 0x114
MDB_REVA = 0x115
MDB_XPND = 0x117

RX=18 #Puerto de la raspberry para recepcion
TX=23 #Puerto de la raspberry para transmision

#Setup de la libreria pigpio
pi = pigpio.pi()	#Inicializa el objeto pigpio
pi.set_mode(TX, pigpio.OUTPUT)	#Elige el pin TX como modo de salida
pi.set_mode(RX, pigpio.INPUT)	#Elige el pin RX como modo de salida

#Creacion de la onda para enviar los datos
pi.wave_clear()	#Se elimina cualquier dato que exista en el buffer
pi.wave_add_serial(TX,9600,'00000000',0,8,2)	# Se crea la onda con 1 bit de start y 1 de stop
wid = pi.wave_create()	# Devuelve el id de la onda creada
pi.bb_serial_read_open(RX,9600,8)	# Abre la lectura de datos 

while True:
	pi.wave_send_once(wid)	#Envia la onda con los datos ya creados 
	#pi.wave_delete(wid)	#Elimina la onda con el dato existente
	while pi.wave_tx_busy():	#Mientras no se haya enviado todos los datos se quedara en el loop
		pass
	
	(count,data) = pi.bb_serial_read(RX)
	print(count)
	print(data)
	time.sleep(2.0)



#free resources
#pi.wave_delete(wid)
pi.bb_serial_read_close(RX)
pi.stop()
