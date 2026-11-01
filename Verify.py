#!/usr/bin/python3
import sys
sys.dont_write_bytecode = True

from checkup.vPort import *
from checkup.levenshtein import *

class Verify:
  def __init__(self):
    self.PIDs = []
    
  def getPIDs(self):
    return self.PIDs
    
  def setPIDs(self):
    #Seulement applée par verifyLevenstein()
    self.PIDs = getPortFromJSON("out/pstree/suspicious_proc.json")
    
  def verifyPort(self,PIDs:list):
    getPortL(PIDs)
    
  def writePort(self):
    writeAll()
    
  def verifyLevenstein(self):
    executeLevenstein()
    self.setPIDs()

