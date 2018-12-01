import webiopi
 
GPIO = webiopi.GPIO
  
RED   = 22
GREEN = 17
BLUE  = 27
   
def setup():
    # Set GPIO to PWM
    GPIO.setFunction(RED  , GPIO.PWM)
    GPIO.setFunction(GREEN, GPIO.PWM)
    GPIO.setFunction(BLUE , GPIO.PWM)
                        
def destroy():
    # Light off
    GPIO.pwmWrite(RED  , 0)
    GPIO.pwmWrite(GREEN, 0)
    GPIO.pwmWrite(BLUE , 0)
