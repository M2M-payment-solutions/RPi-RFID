# Read_loop.py

import RPi.GPIO as GPIO
import SimpleMFRC522 as RF
import requests
import time
import json

rfid = RF.SimpleMFRC522()
url = 'http://139.59.78.46:2800/postdata'

while 1:
	print "place the tag"
	id, text = rfid.read()
	# text = input("enter the data.. >> ")
        print id
	r = requests.post(url, json = {'name': text})
	print r
	print '*******'
	print 'wait...'
	time.sleep(3)
	# t = "hi2"
	# try:
		# print("place the tag...")
  #       # id, text = rfid.read()
  #       payload = {'name': text}
		# print("data sent to server... >>> ")
		# print(r)
		# print("restarting")
		# print("hi")
	# finally:
        # GPIO.cleanup()


