#------------------------------------------------------------------------------ 
# Project          : RMUTR Raspberry Pi to PLC V1 
# VSCode Extension : Python 
# Source           : https://github.com/rmutr/RPi2PLC_V1_Python.git 
# Board            : Raspberry Pi 3 Model B+ 


#------------------------------------------------------------------------------ 
import time 


#------------------------------------------------------------------------------ 
def Sys_Communication():
  return 0

def Sys_ReadDigitalInputs(): 
  return 0 

def Sys_ReadAnalogInputs(): 
  return 0 

def Sys_Process(): 
  return 0

def Sys_WriteDigitalOutputs(): 
  return 0 

def Sys_WriteAnalogOutput(): 
  return 0 

def Sys_Display():
  print("run..") 
  return 0 

def Sys_TimeController():
  time.sleep(1) 
  return 0


#--- Initial hardware & Reset all variables ----------------------------------- 
print("RMUTR Raspberry Pi to PLC V1") 

while True: 

#--- Communication ------------------------------------------------------------ 
  Sys_Communication()

#--- Read digital inputs ------------------------------------------------------ 
  Sys_ReadDigitalInputs()

#--- Read analog inputs ------------------------------------------------------- 
  Sys_ReadAnalogInputs()

#--- Process ------------------------------------------------------------------ 
  Sys_Process()

#--- Write digital outputs ---------------------------------------------------- 
  Sys_WriteDigitalOutputs()

#--- Write analog outputs ----------------------------------------------------- 
  Sys_WriteAnalogOutput()

#--- Display ------------------------------------------------------------------ 
  Sys_Display()

#--- Time controller ---------------------------------------------------------- 
  Sys_TimeController()
