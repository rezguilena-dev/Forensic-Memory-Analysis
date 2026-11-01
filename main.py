#!/usr/bin/python3
import sys
sys.dont_write_bytecode = True

from Verify import *

if __name__ == "__main__":
  print("ok")
  v = Verify()
  """
  Lance l'analyse des processus avec levenstein
  """
  #v.verifyLevenstein()
  
  PIDs = v.getPIDs() #getPIDs() à modifier
  
  """ 
  Recherche de ports ouverts/communication faite par les processus dans la liste PIDs
  """
  #v.verifyPort(PIDs)
  
  """
  Ecriture du résultat de la recherche de ports dans un fichier dans le dossier out/ports
  """
  #v.writePort()
