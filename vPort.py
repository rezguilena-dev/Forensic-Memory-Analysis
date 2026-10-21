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
    print(jsD[i])
    rem.append(jsD[i])

if __name__ == "__main__":
  getPort(6422)
  print(rem)

