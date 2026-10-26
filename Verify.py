#!/usr/bin/python3
import sys
sys.dont_write_bytecode = True

from checkup.vPort import *

class Verify:

  def __init___(self,PIDs:list):
    self.PIDs = PIDs

  def verifyPort(self,PIDs:list):
    getPortL(PIDs)
    
  def writePort(self):
    writeAll()

if __name__ == "__main__":
  print("ok")
  PIDs = [] #liste PID à vérifier
  """ 
  Recherche de ports ouverts/communication faite par les processus dans la liste PIDs
  """
  #verifyPort(PIDs)
  
  """
  Ecriture du résultat de la recherche de ports dans un fichier dans le dossier out/ports
  """
  #writePort()
