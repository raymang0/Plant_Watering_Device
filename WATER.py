#When executed, this program will activate pins connected to the plant watering circuit.
#Once the circuit receives the signals, the water pump solenoid will then release a portion of water.
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print "Now Watering Plant"
GPIO.output(18,GPIO.HIGH) #Sends current through the GPIO pin completing the solenoid circuit.
time.sleep(10) #The current will continue until the sleep timer ends.	
print "Done Watering Plant"
GPIO.output(18,GPIO.LOW) #The GPIO pin will be deactivated here.

