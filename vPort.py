#!/usr/bin/python3
import json
import sys
sys.dont_write_bytecode = True

rem = []

def getPort(PID:int):
  #Verifie si un port à été ouvert par le processsus donné (PID)
  with open('ressources/out/linux.sockstat.json') as jsF :
    jsD = json.load(jsF)
    i = 0
    while jsD[i]['PID'] != PID and i < len(jsD):
      i += 1
    #print(jsD[i])
    if jsD[i]['PID'] == PID:
      rem.append(jsD[i])
    
def getPortL(PIDs:list):
  #Verifie les ports ouverts par une liste de processus donné (PIDs)
  with open('ressources/out/linux.sockstat.json') as jsF :
    jsD = json.load(jsF)
    for pid in PIDs :
      getPort(pid)
      
def getLPort(PID:int):
  #Recupère la liste de tout les ports ouverts par un processus donné (PID)
  with open('ressources/out/linux.sockstat.json') as jsF :
    jsD = json.load(jsF)
    i = 0
    while i < len(jsD):
      if jsD[i]['PID'] == PID:
        rem.append(jsD[i])
      i += 1

if __name__ == "__main__":
  #getPort(6422)
  #getPortL([6422])
  #getLPort(6422)
  #print(len(rem))
  print(rem)
  

