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
  def __init__(self, address, bit): 
    self.address = address 
    self.bit = bit 
    self.value = 0
  


class R_DO_NPN: 
  def __init__(self, address, bit): 
    self.address = address 
    self.bit = bit 
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

def R_AND(*arg):
  result = 1
  for b_AND in arg:
    if b_AND == 0:
      result = 0
  return result

def R_OR(*arg):
  result = 0
  for b_OR in arg:
    if b_OR == 1:
      result = 1
  return result

def R_LDN(*arg):
  result = 1
  for b_LDN in arg:
    if b_LDN == 0:
      result = 0
  return result

def R_ANDN(*arg):
  result = 1
  for b_ANDN in arg:
    if b_ANDN == 0:
      result = 0
  return result

def R_ORN(*arg):
  result = 0
  for b_ORN in arg:
    if b_ORN == 1:
      result = 1
  return result
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

di.append(R_DI_NPN(0x20, 0)) 
di.append(R_DI_NPN(0x20, 1)) 
di.append(R_DI_NPN(0x20, 2)) 
di.append(R_DI_NPN(0x20, 3)) 
di.append(R_DI_NPN(0x20, 4)) 
di.append(R_DI_NPN(0x20, 5)) 
di.append(R_DI_NPN(0x20, 6)) 
di.append(R_DI_NPN(0x20, 7)) 

di.append(R_DI_NPN(0x21, 0)) 
di.append(R_DI_NPN(0x21, 1)) 
di.append(R_DI_NPN(0x21, 2)) 
di.append(R_DI_NPN(0x21, 3)) 
di.append(R_DI_NPN(0x21, 4)) 
di.append(R_DI_NPN(0x21, 5)) 
di.append(R_DI_NPN(0x21, 6)) 
di.append(R_DI_NPN(0x21, 7)) 

di.append(R_DI_NPN(0x22, 0)) 
di.append(R_DI_NPN(0x22, 1)) 
di.append(R_DI_NPN(0x22, 2)) 
di.append(R_DI_NPN(0x22, 3)) 
di.append(R_DI_NPN(0x22, 4)) 
di.append(R_DI_NPN(0x22, 5)) 
di.append(R_DI_NPN(0x22, 6)) 
di.append(R_DI_NPN(0x22, 7)) 

di.append(R_DI_NPN(0x23, 0)) 
di.append(R_DI_NPN(0x23, 1)) 
di.append(R_DI_NPN(0x23, 2)) 
di.append(R_DI_NPN(0x23, 3)) 
di.append(R_DI_NPN(0x23, 4)) 
di.append(R_DI_NPN(0x23, 5)) 
di.append(R_DI_NPN(0x23, 6)) 
di.append(R_DI_NPN(0x23, 7)) 

do.append(R_DO_NPN(0x24, 0)) 
do.append(R_DO_NPN(0x24, 1)) 
do.append(R_DO_NPN(0x24, 2)) 
do.append(R_DO_NPN(0x24, 3)) 
do.append(R_DO_NPN(0x24, 4)) 
do.append(R_DO_NPN(0x24, 5)) 
do.append(R_DO_NPN(0x24, 6)) 
do.append(R_DO_NPN(0x24, 7)) 

do.append(R_DO_NPN(0x25, 0)) 
do.append(R_DO_NPN(0x25, 1)) 
do.append(R_DO_NPN(0x25, 2)) 
do.append(R_DO_NPN(0x25, 3)) 
do.append(R_DO_NPN(0x25, 4)) 
do.append(R_DO_NPN(0x25, 5)) 
do.append(R_DO_NPN(0x25, 6)) 
do.append(R_DO_NPN(0x25, 7)) 

do.append(R_DO_NPN(0x26, 0)) 
do.append(R_DO_NPN(0x26, 1)) 
do.append(R_DO_NPN(0x26, 2)) 
do.append(R_DO_NPN(0x26, 3)) 
do.append(R_DO_NPN(0x26, 4)) 
do.append(R_DO_NPN(0x26, 5)) 
do.append(R_DO_NPN(0x26, 6)) 
do.append(R_DO_NPN(0x26, 7)) 

do.append(R_DO_NPN(0x27, 0)) 
do.append(R_DO_NPN(0x27, 1)) 
do.append(R_DO_NPN(0x27, 2)) 
do.append(R_DO_NPN(0x27, 3)) 
do.append(R_DO_NPN(0x27, 4)) 
do.append(R_DO_NPN(0x27, 5)) 
do.append(R_DO_NPN(0x27, 6)) 
do.append(R_DO_NPN(0x27, 7)) 

bus_dio = smbus.SMBus(1) 

#------------------------------------------------------------------------------ 
def sys_communication(): 
  return 0

def sys_read_digital_inputs(): 
  for bdi in di: 
    bdi.value = 0 

  di_byte[0] = (255 - bus_dio.read_byte(di[0].address)) 

  if (di_byte[0] & 0x01) > 0: 
    di[0].value = 1 

  if (di_byte[0] & 0x02) > 0: 
    di[1].value = 1 

  if (di_byte[0] & 0x04) > 0: 
    di[2].value = 1 

  if (di_byte[0] & 0x08) > 0: 
    di[3].value = 1 

  if (di_byte[0] & 0x10) > 0: 
    di[4].value = 1 

  if (di_byte[0] & 0x20) > 0: 
    di[5].value = 1 

  if (di_byte[0] & 0x40) > 0: 
    di[6].value = 1 

  if (di_byte[0] & 0x80) > 0: 
    di[7].value = 1 

  #di_byte[1] = (255 - bus_dio.read_byte(di[8].address)) 

  if (di_byte[1] & 0x01) > 0: 
    di[8].value = 1 

  if (di_byte[1] & 0x02) > 0: 
    di[9].value = 1 

  if (di_byte[1] & 0x04) > 0: 
    di[10].value = 1 

  if (di_byte[1] & 0x08) > 0: 
    di[11].value = 1 

  if (di_byte[1] & 0x10) > 0: 
    di[12].value = 1 

  if (di_byte[1] & 0x20) > 0: 
    di[13].value = 1 

  if (di_byte[1] & 0x40) > 0: 
    di[14].value = 1 

  if (di_byte[1] & 0x80) > 0: 
    di[15].value = 1 

  #di_byte[2] = (255 - bus_dio.read_byte(di[16].address)) 

  if (di_byte[2] & 0x01) > 0: 
    di[16].value = 1 

  if (di_byte[2] & 0x02) > 0: 
    di[17].value = 1 

  if (di_byte[2] & 0x04) > 0: 
    di[18].value = 1 

  if (di_byte[2] & 0x08) > 0: 
    di[19].value = 1 

  if (di_byte[2] & 0x10) > 0: 
    di[20].value = 1 

  if (di_byte[2] & 0x20) > 0: 
    di[21].value = 1 

  if (di_byte[2] & 0x40) > 0: 
    di[22].value = 1 

  if (di_byte[2] & 0x80) > 0: 
    di[23].value = 1 

  #di_byte[3] = (255 - bus_dio.read_byte(di[24].address)) 

  if (di_byte[3] & 0x01) > 0: 
    di[24].value = 1 

  if (di_byte[3] & 0x02) > 0: 
    di[25].value = 1 

  if (di_byte[3] & 0x04) > 0: 
    di[26].value = 1 

  if (di_byte[3] & 0x08) > 0: 
    di[27].value = 1 

  if (di_byte[3] & 0x10) > 0: 
    di[28].value = 1 

  if (di_byte[3] & 0x20) > 0: 
    di[29].value = 1 

  if (di_byte[3] & 0x40) > 0: 
    di[30].value = 1 

  if (di_byte[3] & 0x80) > 0: 
    di[31].value = 1 



  return 0 

def sys_read_analog_inputs(): 
  return 0 

def sys_process(): 
  #for bdo in do: 
  #  bdo.toggle()

  do[0].value = R_AND(di[0].value, di[1].value, di[2].value)
  do[1].value = R_OR(di[0].value, di[1].value, di[2].value)
  do[2].value = R_LDN(not di[0].value, di[1].value, di[2].value)
  do[0].value = R_ANDN(di[0].value, not di[1].value, not di[2].value)
  do[1].value = R_ORN(not di[0].value, not di[1].value, not di[2].value)
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

  bus_dio.write_byte(do[0].address, (255 - do_byte[0])) 

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

  #bus_dio.write_byte(do[8].address, (255 - do_byte[1])) 

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

  #bus_dio.write_byte(do[16].address, (255 - do_byte[2])) 

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

  #bus_dio.write_byte(do[24].address, (255 - do_byte[3])) 

  return 0 

def sys_write_analog_output(): 
  return 0 

def sys_display(): 
  print(str(di[7].value) + str(di[6].value) + str(di[5].value) + str(di[4].value) + " " + str(di[3].value) + str(di[2].value) + str(di[1].value) + str(di[0].value)) 
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
  
  
