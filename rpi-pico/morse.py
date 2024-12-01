from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT, value=0)

msg = "... --- ..."  # SOS

while True:
    for ch in msg:
        if ch == ".":
            led.on()
            sleep(0.2)
            led.off()
            sleep(0.2)
        elif ch == "-":
            led.on()
            sleep(0.6)
            led.off()
            sleep(0.2)
        else:
            sleep(0.4)
    sleep(2)
