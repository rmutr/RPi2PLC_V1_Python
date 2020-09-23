import smbus
import time

LED1 = 0x01
LED2 = 0x02
LED3 = 0x04
LED4 = 0x08

bus = smbus.SMBus(1)


while True:
    print("fffff")
    bus.write_byte(0x20, LED1)
    time.sleep(1)
    bus.write_byte(0x20, LED2)
    time.sleep(1)
    bus.write_byte(0x20, LED3)
    time.sleep(1)
    bus.write_byte(0x20, LED4)
    time.sleep(1)
