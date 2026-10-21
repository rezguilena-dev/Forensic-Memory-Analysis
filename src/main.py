import json
#Calculer la distance de levenshtein
def levenshtein(a,b):
    n = len(a)
    m = len(b)

    mat=[[0]*(m+1) for _ in range(n+1)]

    for i in range (n+1):
        mat[i][0] = i
    for j in range (m+1):
        mat[0][j] = j
    for i in range(1,n+1):
        for j in range(1,m+1):
            cout = 0 if a[i-1] == b[j-1] else 1
            mat[i][j] = min(mat[i-1][j]+1 ,mat[i][j-1]+1,mat[i-1][j-1]+cout)
    return mat[n][m]

#Parcourir le Json
safeProcess=[  "systemd","systemd-journal","systemd-udevd","systemd-oomd",
    "systemd-resolve","systemd-timesyn","systemd-logind","(sd-pam)",
    "cron","crond","sh","bash","dash","sudo","su","ssh","sshd",
    "ssh-agent","dbus-daemon","NetworkManager","rsyslogd","snapd",
    "snap","polkitd","cupsd","gdm3","gnome-shell","gnome-session-b",
    "firefox","sublime_text","netstat","ss","ps","top","ls",
    "ping","curl","wget","python3","vmtoolsd","unattended-upgr",
]
safePro =set(safeProcess)
def traverse(node):
    if node["PID"] == 2:                 
        return None
    name = node["COMM"]
    found = False
    if name not in safePro:
            threshold = 1 if len(name)<=4 else 2
            for proc in safeProcess:
                distance = levenshtein(name,proc)
                if 1<= distance <= threshold:
                    found = True
                    break 
    keptChildren=[]
    for child in node["__children"]:
        res= traverse(child)
        if res is not None :
            keptChildren.append(res)
    if found : # si mon noeud est suspect 
        return node.copy()  
    if keptChildren : #mon noeud est safe mais un de ses fils est suspect
        path = node.copy()
        path["__children"] = keptChildren
        return path
    return None #aucun noeud suspect


    






if __name__ == '__main__':
    with open("../ressources/out/linux.pstree.json") as file:
        data = json.load(file)
    result =[]
    for node in data :
        res= traverse(node)
        if res is not None:
            result.append(res)

    with open("./JSON FILES/suspects.json", "w") as f:
        json.dump(result, f, indent=4)