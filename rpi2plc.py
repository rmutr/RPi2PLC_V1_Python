#------------------------------------------------------------------------------ 
# Project          : RMUTR Raspberry Pi to PLC V1 
# VSCode Extension : Python 
# Source           : https://github.com/rmutr/RPi2PLC_V1_Python.git 
# Board            : Raspberry Pi 3 Model B+ 


#------------------------------------------------------------------------------ 
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

  def update(self): 
    return 0 

  def off(self): 
    self.value = 0 
    self.update() 
    return 0 

  def on(self): 
    self.value = 1 
    self.update() 
    return 0 

  def toggle(self): 
    if self.value == 0: 
      self.value = 1 
    else: 
      self.value = 0 
    self.update() 
    return 0 

class R_ADC: 
  def __init__(self, ai_pin): 
    self.ai_pin = ai_pin 

class R_DAC: 
  def __init__(self, ao_pin): 
    self.ao_pin = ao_pin 


#------------------------------------------------------------------------------ 
do_00 = R_DO_NPN(0x20, 0) 
do_01 = R_DO_NPN(0x20, 1) 
do_02 = R_DO_NPN(0x20, 2) 
do_03 = R_DO_NPN(0x20, 3) 
do_04 = R_DO_NPN(0x20, 4) 
do_05 = R_DO_NPN(0x20, 5) 
do_06 = R_DO_NPN(0x20, 6) 
do_07 = R_DO_NPN(0x20, 7) 

do_08 = R_DO_NPN(0x21, 0) 
do_09 = R_DO_NPN(0x21, 1) 
do_10 = R_DO_NPN(0x21, 2) 
do_11 = R_DO_NPN(0x21, 3) 
do_12 = R_DO_NPN(0x21, 4) 
do_13 = R_DO_NPN(0x21, 5) 
do_14 = R_DO_NPN(0x21, 6) 
do_15 = R_DO_NPN(0x21, 7) 

do_16 = R_DO_NPN(0x22, 0) 
do_17 = R_DO_NPN(0x22, 1) 
do_18 = R_DO_NPN(0x22, 2) 
do_19 = R_DO_NPN(0x22, 3) 
do_20 = R_DO_NPN(0x22, 4) 
do_21 = R_DO_NPN(0x22, 5) 
do_22 = R_DO_NPN(0x22, 6) 
do_23 = R_DO_NPN(0x22, 7) 

do_24 = R_DO_NPN(0x23, 0) 
do_25 = R_DO_NPN(0x23, 1) 
do_26 = R_DO_NPN(0x23, 2) 
do_27 = R_DO_NPN(0x23, 3) 
do_28 = R_DO_NPN(0x23, 4) 
do_29 = R_DO_NPN(0x23, 5) 
do_30 = R_DO_NPN(0x23, 6) 
do_31 = R_DO_NPN(0x23, 7) 


#------------------------------------------------------------------------------ 
def sys_communication(): 
  return 0

def sys_read_digital_inputs(): 
  return 0 

def sys_read_analog_inputs(): 
  return 0 

def sys_process(): 
  return 0

def sys_write_digital_outputs(): 
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

