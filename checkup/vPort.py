#!/usr/bin/python3
import json
import sys
sys.dont_write_bytecode = True

rem = {}

def getPort(PID:int):
  #Verifie si un port à été ouvert par le processsus donné (PID)
  with open('ressources/out/linux.sockstat.json') as jsF :
    jsD = json.load(jsF)
    i = 0
    while jsD[i]['PID'] != PID and i < len(jsD):
      i += 1
    if jsD[i]['PID'] == PID:
      return True
  return False

def getPortL(PIDs:list):
  #Verifie les ports ouverts par une liste de processus donné (PIDs)
  with open('ressources/out/linux.sockstat.json') as jsF :
    jsD = json.load(jsF)
    for pid in PIDs :
      getLPort(pid)
      
def getLPort(PID:int):
  #Recupère la liste de tout les ports ouverts par un processus donné (PID)
  l = []
  with open('ressources/out/linux.sockstat.json') as jsF :
    jsD = json.load(jsF)
    i = 0
    while i < len(jsD):
      if jsD[i]['PID'] == PID:
        l.append(jsD[i])
      i += 1
  rem[PID] = l

def writeFile(PID:int):
  #Ecrit le contenu de rem[PID] dans un fichier process{numProcess}.json
  try:
     f = open(f"out/ports/process{PID}.json", "x")
  except:
    #overwriting
    with open(f"out/ports/process{PID}.json", "w") as f:
      json.dump(rem[PID],f,ensure_ascii=False, indent=2)
  else :
    #adding
    with open(f"out/ports/process{PID}.json", "a") as f:
      json.dump(rem[PID],f,ensure_ascii=False, indent=2)
      
def writeAll(PIDs:list):
  for r in rem :
    writeFile(r)

 
