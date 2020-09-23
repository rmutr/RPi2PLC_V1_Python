import smbus
import time

SW1 = 0x01

bus = smbus.SMBus(1)
while True:

  SW1 = bus.read_byte(0x20)
  print (SW1)

