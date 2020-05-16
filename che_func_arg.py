import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
R_DO = 0


def f_input(*input):  
    for value in input:  
        print(value) 

while True:
        
    #
    X1 = GPIO.input(17)
    X2 = GPIO.input(18)
    
    A = (X1, X2)
    f_input(*A)
    
      
    #GPIO.output(21, R_DO)    
    
        

