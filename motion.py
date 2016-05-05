import RPi.GPIO as GPIO
import time

max_timeout_s = 120
last_motion = 0
is_motion = False

GPIO.setmode(GPIO.BCM)
PIR_PIN = 24
RLS_PIN = 23
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(RLS_PIN, GPIO.OUT)

def logMsg(msg):
    print '[' + time.ctime() + '] ' + msg

def OnMotion(PIR_PIN):
        global last_motion
        global is_motion
        is_motion = GPIO.input(PIR_PIN)
        if is_motion:
                last_motion = time.time()
                logMsg("Motion detected!")
                if GPIO.input(RLS_PIN):
                        GPIO.output(RLS_PIN, GPIO.LOW)
                logMsg("Power ON")
        else:
                logMsg("No one there")

logMsg("Motion Controlled Power Module")
time.sleep(2)
logMsg("Ready")

try:
        is_motion = GPIO.input(PIR_PIN)
        last_motion = time.time()
        if(is_motion):
                GPIO.output(RLS_PIN, GPIO.LOW)
        else:
                GPIO.output(RLS_PIN, GPIO.HIGH)
        GPIO.add_event_detect(PIR_PIN, GPIO.BOTH, callback=OnMotion, bouncetime=300)
        while 1:
                if(not is_motion and not GPIO.input(RLS_PIN) and (time.time() - last_motion) >= max_timeout_s):
                        GPIO.output(RLS_PIN, GPIO.HIGH)
                        logMsg("Power OFF")
                        time.sleep(1)
except KeyboardInterrupt:
        logMsg("Quit")
        GPIO.cleanup()
