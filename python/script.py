import webiopi
import datetime

webiopi.setDebug()
GPIO = webiopi.GPIO

R=17
G=27
B=22
HOUR_ON = datetime.time(0,0)
HOUR_OFF = datetime.time(0,0)

def setup():
    webiopi.debug("Script with macros - Setup")
    
    GPIO.setFunction(R, GPIO.OUT)
    GPIO.output(R, GPIO.LOW)
    GPIO.setFunction(G, GPIO.OUT)
    GPIO.output(G, GPIO.LOW)
    GPIO.setFunction(B, GPIO.OUT)
    GPIO.output(B, GPIO.LOW)

def loop():
    now = datetime.time(datetime.datetime.now().hour, datetime.datetime.now().minute)
    webiopi.sleep(1)
    
    # Automatically switch on LED
    if ((now.hour == HOUR_ON.hour) and (now.minute == HOUR_ON.minute) and (now.second == 0)):
        if (GPIO.digitalRead(G) == GPIO.HIGH):
            GPIO.digitalWrite(G, GPIO.LOW)
 
    # Automatically switch off LED
    if ((now.hour == HOUR_OFF.hour) and (now.minute == HOUR_OFF.minute) and (now.second == 0)):
        if (GPIO.digitalRead(G) == GPIO.LOW):
            GPIO.digitalWrite(G, GPIO.HIGH)

def destroy():
    webiopi.debug("Script with macros - Destroy")
    GPIO.setFunction(R, GPIO.IN)
    GPIO.setFunction(G, GPIO.IN)
    GPIO.setFunction(B, GPIO.IN)
    
@webiopi.macro
def getLightHours():
    return "%s;%s" % (HOUR_ON.strftime("%H:%M"),HOUR_OFF.strftime("%H:%M"))
 
@webiopi.macro
def setLightHours(on, off):
    global HOUR_ON, HOUR_OFF
    # Partition out arguments
    array_on  = on.split(":")
    array_off = off.split(":")
    # Setting values
    HOUR_ON  = datetime.time(int(array_on[0]),int(array_on[1]))
    HOUR_OFF = datetime.time(int(array_off[0]),int(array_off[1]))
    return getLightHours()
    
    

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
def morningMode():
    GPIO.output(R, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(B, GPIO.LOW)

@webiopi.macro
def readMode():
    GPIO.output(R, GPIO.LOW)
    GPIO.output(G, GPIO.LOW)
    GPIO.output(B, GPIO.HIGH)

@webiopi.macro
def ledOff():
    GPIO.output(R, GPIO.HIGH)
    GPIO.output(G, GPIO.HIGH)
    GPIO.output(B, GPIO.HIGH)

