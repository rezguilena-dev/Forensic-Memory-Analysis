#!/usr/bin/python3
import sys
sys.dont_write_bytecode = True
from vPort import *

if __name__ == "__main__":
  print("ok")
  PID = 6422
  PIDs = [6422,1]
  #print(getPort(PID)) #OK
  #getPortL([PID]) #OK
  #getLPort(PIDs[0]) #OK
  getPortL(PIDs)
  
  #print(rem)
  
  writeAll(PIDs)
