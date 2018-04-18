import machine
import ssd1306
import dht
import time

sw = machine.Pin(0, machine.Pin.OUT)
d = dht.DHT22(machine.Pin(2))

while True:
    time.sleep(2)
    d.measure()
    temp = d.temperature()
    if temp > 22:
        sw.on()
    elif temp < 20:
        sw.off()
    time.sleep(60)
