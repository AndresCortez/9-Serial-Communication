#!/usr/bin/env python
import sys
import time
import difflib

import pigpio
          
# Constantes 
MDB_ACK  = 0
MDB_RST  = 0x10
MDB_STP  = 0x11
MDB_POLL = 0x12
MDB_VEND = 0x13
MDB_READ = 0x14
MDB_REVA = 0x15
MDB_XPND = 0x17
			
# Enteros 
byte_9 = 0
chksum_vmc = 0
chksum = 0 
in = 0
poll = 0
c = 0 
set_up = 0
fondos = 0
			
# Cadenas
binario = ""
buff = ""
*cash_id="CITXPEND-IT0001CASHLESS201401" preguntar bien que es esto 

#Setup del serial

pi = pigpio.pi()
pi.set_mode(TX, pigpio.OUTPUT)
pi.set_mode(RX, pigpio.INPUT)
# fatal exceptions off (so that closing an unopened gpio doesn't error)

pigpio.exceptions = False

pi.bb_serial_read_close(RX)

# fatal exceptions on

pigpio.exceptions = True

# create a waveform representing the serial data

pi.wave_clear()
pi.wave_add_serial(TX,9600,b'\x00\x01',0,9,2)
ack=pi.wave_create()
pi.wave_add_serial(TX,9600,b'\x00\x00',0,9,2)
ack0=pi.wave_create()
pi.wave_add_serial(TX,9600,b'\x10\x01',0,9,2)
rst=pi.wave_create()
pi.wave_add_serial(TX,9600,b'\x11\x01',0,9,2)
stp=pi.wave_create()
pi.wave_add_serial(TX,9600,b'\x12\x01',0,9,2)
poll=pi.wave_create()
pi.wave_add_serial(TX,9600,b'\x13\x01',0,9,2)
vend=pi.wave_create()
pi.wave_add_serial(TX,9600,b'\x14\x01',0,9,2)
read=pi.wave_create()
pi.wave_add_serial(TX,9600,b'\x15\x01',0,9,2)
reva=pi.wave_create()
pi.wave_add_serial(TX,9600,b'\x16\x01',0,9,2)
xpnd=pi.wave_create()

############## Venta ######################
pi.wave_add_serial(TX,9600,b'\x11\x00',0,9,2)
ack=pi.wave_create()
pi.wave_add_serial(TX,9600,b'\xFF\x00',0,9,2)
ack0=pi.wave_create()
pi.wave_add_serial(TX,9600,b'\xFF\x00',0,9,2)
rst=pi.wave_create()
pi.wave_add_serial(TX,9600,b'\x11\x01',0,9,2)
stp=pi.wave_create()

#############################################################


	
#Definir todos los casos de switch 


def mdb_poll:
	if(not poll):
		count = -1
		while(count == -1)
			(count,data) = pi.bb_serial_read(RX)
			chksum_vmc = data
			chksum = 0
			pi.wave_send_once(ack0)
			while pi.wave_tx_busy();
				pass
			pi.wave_send_once(ack)
			while pi.wave_tx_busy();
				pass
			
		count = -1
		while(count == -1)
			(count,data) = pi.bb_serial_read(RX)
			byte_9 = data
		
		print ("Recibi por MDB (POLL 1)")
		 #Serial.print("Recibi por MDB (POLL 1) -> 0x");
		 #Serial.print((byte_9 >> 8)& 0x00ff, HEX);
		 #Serial.print(byte_9 & 0x00ff, HEX);
		 #Serial.print(" (");
		 #Serial.print(byte_9);
		 #Serial.println(")");
		poll = 1
	else:
		if (fondos > 0):
			count = -1
			while(count == -1)
				(count,data) = pi.bb_serial_read(RX)
				chksum_vmc = data
			pi.wave_send_once(ack)
			while pi.wave_tx_busy();
				pass
			print ("Envie un ACK")
		else: 
			while (not ser.inWaiting()):
			count = -1
			while(count == -1)
				(count,data) = pi.bb_serial_read(RX)
				chksum_vmc = data
			chksum = 0;
			
			#Mandamos la venta
			
			#manda_MDB(3,0)
			#manda_MDB(255,0)
			#manda_MDB(255,0)
			#manda_MDB(chksum,1)
			
	
def default:
	print ("Recibi de MDB ->" + data) 
	#default: Serial.print("Recibi de MDB -> 0x");
	#Serial.print((byte_9 >> 8)& 0x00ff, HEX);
	#Serial.print(byte_9 & 0x00ff, HEX);
	#Serial.print(" (");
	#Serial.print(byte_9);
	#Serial.println(")"); break;
	
	
	
	
		

while 1:
	count = -1	
	if count == -1 :
		(count,data) = pi.bb_serial_read(RX)
		while count not - 1:
			byte_9 = data
			#Aqui agregar la entrada de dinero  es decir los fondos 
			#fondos = digitalRead(48)
			def switch(byte_9[0])
				return{
					MDB_RST  : mdb_rst,
					MDB_POLL : mdb_poll,
					MDB_STP  : mdb_stp,
					MDB_XPND : mdb_xpnd,
					MDB_READ : mdb_read,
					MDB_REVA : mdb_reva,
					MDB_VEND : mdb_vend,
				}.get(byte_9, default)
					
			
			   
			   
			   
			   
			   
