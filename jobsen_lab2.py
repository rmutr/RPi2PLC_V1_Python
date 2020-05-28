  #------------------------------------------------------------------------------ 
# Project          : RMUTR Raspberry Pi to PLC V1 
# VSCode Extension : Python 
# Source           : https://github.com/rmutr/RPi2PLC_V1_Python.git 
# Board            : Raspberry Pi 3 Model B+ 


#------------------------------------------------------------------------------ 
import smbus 
import time 


#------------------------------------------------------------------------------ 
class R_DI_NPN: 
  def __init__(self, di_address, di_bit): 
    self.di_address = di_address 
    self.di_bit = di_bit 

class R_DO_NPN: 
  def __init__(self, do_address, do_bit): 
    self.do_address = do_address 
    self.do_bit = do_bit 
    self.value = 0 

  def off(self): 
    self.value = 0 
    return 0 

  def on(self): 
    self.value = 1 
    return 0 

  def toggle(self): 
    if self.value == 0: 
      self.value = 1 
    else: 
      self.value = 0 

    #self.value != self.value 
    return 0 

class R_ADC: 
  def __init__(self, ai_pin): 
    self.ai_pin = ai_pin 

class R_DAC: 
  def __init__(self, ao_pin): 
    self.ao_pin = ao_pin 


#------------------------------------------------------------------------------ 
di = [] #<- faster than di = list() 
do = [] 
ai = [] 
ao = [] 

di_byte = [] 
di_byte.append(0)
di_byte.append(0)
di_byte.append(0)
di_byte.append(0)

do_byte = [] 
do_byte.append(0) 
do_byte.append(0) 
do_byte.append(0) 
do_byte.append(0) 

do.append(R_DO_NPN(0x20, 0)) 
do.append(R_DO_NPN(0x20, 1)) 
do.append(R_DO_NPN(0x20, 2)) 
do.append(R_DO_NPN(0x20, 3)) 
do.append(R_DO_NPN(0x20, 4)) 
do.append(R_DO_NPN(0x20, 5)) 
do.append(R_DO_NPN(0x20, 6)) 
do.append(R_DO_NPN(0x20, 7)) 

do.append(R_DO_NPN(0x21, 0)) 
do.append(R_DO_NPN(0x21, 1)) 
do.append(R_DO_NPN(0x21, 2)) 
do.append(R_DO_NPN(0x21, 3)) 
do.append(R_DO_NPN(0x21, 4)) 
do.append(R_DO_NPN(0x21, 5)) 
do.append(R_DO_NPN(0x21, 6)) 
do.append(R_DO_NPN(0x21, 7)) 

do.append(R_DO_NPN(0x22, 0)) 
do.append(R_DO_NPN(0x22, 1)) 
do.append(R_DO_NPN(0x22, 2)) 
do.append(R_DO_NPN(0x22, 3)) 
do.append(R_DO_NPN(0x22, 4)) 
do.append(R_DO_NPN(0x22, 5)) 
do.append(R_DO_NPN(0x22, 6)) 
do.append(R_DO_NPN(0x22, 7)) 

do.append(R_DO_NPN(0x23, 0)) 
do.append(R_DO_NPN(0x23, 1)) 
do.append(R_DO_NPN(0x23, 2)) 
do.append(R_DO_NPN(0x23, 3)) 
do.append(R_DO_NPN(0x23, 4)) 
do.append(R_DO_NPN(0x23, 5)) 
do.append(R_DO_NPN(0x23, 6)) 
do.append(R_DO_NPN(0x23, 7)) 

hw_do = smbus.SMBus(1) 

#------------------------------------------------------------------------------ 
def sys_communication(): 
  return 0

def sys_read_digital_inputs(): 
  return 0 

def sys_read_analog_inputs(): 
  return 0 

def sys_process(): 
  for bdo in do: 
    bdo.toggle() 
  
  return 0

def sys_write_digital_outputs(): 
  do_byte[0] = 0 

  if do[0].value == 1: 
    do_byte[0] += 1 

  if do[1].value == 1 : 
    do_byte[0] += 2 

  if do[2].value == 1: 
    do_byte[0] += 4 

  if do[3].value == 1: 
    do_byte[0] += 8 

  if do[4].value == 1: 
    do_byte[0] += 16 

  if do[5].value == 1: 
    do_byte[0] += 32 

  if do[6].value == 1: 
    do_byte[0] += 64 

  if do[7].value == 1: 
    do_byte[0] += 128 

  hw_do.write_byte(do[0].do_address, (255 - do_byte[0])) 

  do_byte[1] = 0 

  if do[8].value == 1: 
    do_byte[1] += 1 

  if do[9].value == 1 : 
    do_byte[1] += 2 

  if do[10].value == 1: 
    do_byte[1] += 4 

  if do[11].value == 1: 
    do_byte[1] += 8 

  if do[12].value == 1: 
    do_byte[1] += 16 

  if do[13].value == 1: 
    do_byte[1] += 32 

  if do[14].value == 1: 
    do_byte[1] += 64 

  if do[15].value == 1: 
    do_byte[1] += 128 

  #hw_do.write_byte(do[8].do_address, (255 - do_byte[1])) 

  do_byte[2] = 0 

  if do[16].value == 1: 
    do_byte[2] += 1 

  if do[17].value == 1 : 
    do_byte[2] += 2 

  if do[18].value == 1: 
    do_byte[2] += 4 

  if do[19].value == 1: 
    do_byte[2] += 8 

  if do[20].value == 1: 
    do_byte[2] += 16 

  if do[21].value == 1: 
    do_byte[2] += 32 

  if do[22].value == 1: 
    do_byte[2] += 64 

  if do[23].value == 1: 
    do_byte[2] += 128 

  #hw_do.write_byte(do[16].do_address, (255 - do_byte[2])) 

  do_byte[3] = 0 

  if do[24].value == 1: 
    do_byte[3] += 1 

  if do[25].value == 1 : 
    do_byte[3] += 2 

  if do[26].value == 1: 
    do_byte[3] += 4 

  if do[27].value == 1: 
    do_byte[3] += 8 

  if do[28].value == 1: 
    do_byte[3] += 16 

  if do[29].value == 1: 
    do_byte[3] += 32 

  if do[30].value == 1: 
    do_byte[3] += 64 

  if do[31].value == 1: 
    do_byte[3] += 128 

  #hw_do.write_byte(do[8].do_address, (255 - do_byte[3])) 

  return 0 

def sys_write_analog_output(): 
  return 0 

def sys_display():
  print("Run..") 
  return 0 

def sys_time_controller():
  time.sleep(1) 
  return 0


#--- Initial hardware & Reset all variables ----------------------------------- 
print("RMUTR Raspberry Pi to PLC V1") 

while True: 

#--- Communication ------------------------------------------------------------ 
  sys_communication()

#--- Read digital inputs ------------------------------------------------------ 
  sys_read_digital_inputs()

#--- Read analog inputs ------------------------------------------------------- 
  sys_read_analog_inputs()

#--- Process ------------------------------------------------------------------ 
  sys_process()

#--- Write digital outputs ---------------------------------------------------- 
  sys_write_digital_outputs()

#--- Write analog outputs ----------------------------------------------------- 
  sys_write_analog_output()

#--- Display ------------------------------------------------------------------ 
  sys_display()

#--- Time controller ---------------------------------------------------------- 
  sys_time_controller()
  
  
