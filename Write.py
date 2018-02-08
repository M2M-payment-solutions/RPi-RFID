mport RPi.GPIO as GPIO
import SimpleMFRC522 as RF

rfid = RF.SimpleMFRC522()

try:
        text = raw_input('New data:')
        print("Place the tag to write...")
        rfid.write(text)
        print("Written !")
finally:
        GPIO.cleanup()
