import webiopi

webiopi.setDebug()
GPIO = webiopi.GPIO

R=17
G=27
B=22

def setup():
    webiopi.debug("Script with macros - Setup")
    GPIO.setFunction(R, GPIO.OUT)
    GPIO.output(R, GPIO.LOW)
    GPIO.setFunction(G, GPIO.OUT)
    GPIO.output(G, GPIO.LOW)
    GPIO.setFunction(B, GPIO.OUT)
    GPIO.output(B, GPIO.LOW)

def loop():
    webiopi.sleep(1)

def destroy():
    webiopi.debug("Script with macros - Destroy")
    GPIO.setFunction(R, GPIO.IN)
    GPIO.setFunction(G, GPIO.IN)
    GPIO.setFunction(B, GPIO.IN)

@webiopi.macro
def redOn():
    GPIO.output(R, GPIO.LOW)
    GPIO.output(G, GPIO.HIGH)
    GPIO.output(B, GPIO.HIGH)

@webiopi.macro
def greenOn():
    GPIO.output(R, GPIO.HIGH)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(B, GPIO.HIGH)

@webiopi.macro
def blueOn():
    GPIO.output(R, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    GPIO.output(B, GPIO.LOW)

@webiopi.macro
def ledOff():
    GPIO.output(R, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    GPIO.output(B, GPIO.HIGH)

