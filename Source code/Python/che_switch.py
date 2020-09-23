import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
led = 0

while True:
         
    #
    sw1 = GPIO.input(17)
    sw2 = GPIO.input(18)
    
    #
    if(sw1 == 1):
        #GPIO.output(21, GPIO.HIGH)
        led = 1
    if(sw2 == 1):
        #GPIO.output(21, GPIO.LOW)
        led = 0
        
    #    
    GPIO.output(21, led)    
    
        