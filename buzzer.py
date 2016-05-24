import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.OUT)
print ("buzzer on")
GPIO.output(40,GPIO.HIGH)
time.sleep(3)
print ("buzzer off")
GPIO.output(40,GPIO.LOW) 
