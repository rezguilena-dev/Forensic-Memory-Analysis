
import json
import shlex
import os

systemPath = [
    "/usr/bin/", "/usr/sbin/", "/bin/", "/sbin/",
    "/usr/lib/", "/usr/libexec/", "/lib/", "/snap/",
    "/usr/local/bin/", "/usr/local/sbin/"
]


def searchProgram(args):
    #Formats à étudier : 
    #sudo ./programme
    #sudo /absolu
    #sudo options programme #A FAIRE ULTERIEUREMENT POUR DAUTRES DUMP 
    index=0
    while index < len(args) and os.path.basename(args[index])== "sudo":
        index += 1
    program=args[index]
    if program.startswith(("./", "/", "../")):
            return program
    return None

#verifier si c un chemin systeme
def isSystemPath(program):
    program =os.path.normpath(program)
    for path in systemPath :
        path = os.path.normpath(path) #je retire le / a la fin
        if program == path or program.startswith(path +"/") :
            return True
    return False



def analyzePsaux(data):
    result = []
    seen =set() #programmes+PID  deja traités le meme programme peut etre lancé par different pid
    stats ={
        "total":len(data),
        "analyzed" : 0,
        "suspected" :0,
    }
    for proc in data:
        line = proc.get("ARGS", "")
        if not line:
            continue

        args = shlex.split(line)
        #skip les threads
        if not args or args[0].startswith("["):
            continue
        #commandes sans arguments
        if len(args) == 1 : 
            continue 
        
        program = searchProgram(args)
        if program is None : 
            continue
        pid = proc.get("PID")
        key = (pid,program)
        if key not in seen :
            seen.add(key)
            stats["analyzed"] += 1
            # Cas 1 : chemin absolu
            if os.path.isabs(program):
                if not isSystemPath(program):
                    result.append({
                        "PID": pid,
                        "PPID": proc.get("PPID"),
                        "ARGS": line,
                        "programme": program,
                        "raison": "Executable hors des chemins systeme"
                    })

            # Cas 2 : chemin relatif explicite
            #verifier le bash ensuite
            else :
                result.append({
                    "PID": pid,
                    "PPID": proc.get("PPID"),
                    "ARGS": line,
                    "programme": program,
                    "raison": "Chemin relatif a verifier dans l'historique Bash"
                })
    stats["suspected"]=len(result)                   
    return result,stats

if __name__ == "__main__":
    with open("ressources/out/linux.psaux.json") as file:
        data = json.load(file)
    result,stats = analyzePsaux(data)
    print(f"Total processes: {stats['total']}")
    print(f"Programs analyzed: {stats['analyzed']}")
    print(f"Suspicious programs found: {stats['suspected']}")
    with open("./out/psaux/suspicious_path.json", "w") as f:
        json.dump(result, f, indent=4)
