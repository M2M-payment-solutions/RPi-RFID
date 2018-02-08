
import RPi.GPIO as GPIO
import SimpleMFRC522 as RF

rfid = RF.SimpleMFRC522()

try:
        id, text = rfid.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()
