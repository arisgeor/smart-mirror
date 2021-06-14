#!/usr/bin/python3

import serial
import os
import time

def connect_scale():
    if not os.path.exists('/dev/rfcomm0'):
	path = 'sudo rfcomm bind 0 98:D3:71:F6:1A:30' #arduino address 
	os.system (path)
	time.sleep(1)

    bluetoothSerial = serial.Serial( "/dev/rfcomm0", baudrate=9600 )
    return bluetoothSerial
    
def get_scale(BTSerial, threshold):
    try:
        RXData = (BTSerial.readline()).strip().decode("utf-8")
        if float(RXData)>threshold:
           print (RXData)
           return RXData
    except KeyboardInterrupt:
        print('keyboard interrupt detected, exititng...')
        exit()
