import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

 

def f_input(**input):
    for name, value in input.items():
        print("%s = %d" %(name, value))
##        print("{} = {}" .format(name, value))
    

while True:
        
    #
    X1 = GPIO.input(17)
    X2 = GPIO.input(18)
    
    A = {"R_DIO_X1" : X1, "R_DIO_X2" : X1, "R_DIO_X3" : X2, "R_DIO_X4" : X2}
    f_input(**A)
        



