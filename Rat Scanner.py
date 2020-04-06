import os
import sys
import cursor

def getStrings(filename):
    strings = []
    validChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+{}:"|<>?'
    try:
        with open(filename, errors="ignore") as f:
            for i in f.read().splitlines():
                string = ''
                for c in list(i):
                    if c in validChars:
                        string += c
                if len(string) != 0:
                    strings.append(string.lower())
        return strings
    except:
        return strings

def dirAllFP(path):
    #Get file paths and names
    filesList = []
    for dirpath, subdirs, files in os.walk(path):
        for x in files:
            filesList.append(os.path.join(dirpath, x))
    return filesList

def checkStrings(stringList):
    status = False
    infectedStrings = [
        "ddoshttpflood",
        "nanocoreclient",
        "redirectstandarderrorfilenamecmdexeuseshellexecute",
        "errorwritingtotheregistrycannotdeletekey",
        "chromestoredloginsfound",
        "destroy4imagelist",
        "pjoao1578",
        "onlyinstallthisclientfromsourcesyoutrust",
        "disabletaskmgr1"]
    for infstring in infectedStrings:
        for string in stringList: 
            if infstring in string:
                status = True
                break
    return status

#Startup messages
print("RAT(Remote Access Tool) Scanner | v1.0.5.3")
print("Created by: @IWickGames")
print("\n")
print("""Welcome to RAT Scanner
This is a tool to scan and detect Remote Access Tools or Rats
on your computer and attempt to remove them if possible.

To get started first select your scan type

Quick(Q)
Only Scanns the user profile

Full(F)
Scans the entire C:\\ drive

Custom(C)
Enter a custom directory to scan
\n\n
""")

enterValue = input("Select one of the options above[Q/F/C]: ").lower()
if enterValue == "f":
    print("[*] Indexing your system...")
    savedFiles = dirAllFP("C:\\")
elif enterValue == "q":
    print("[*] Indexing your system...")
    savedFiles = dirAllFP("C:\\Users\\" + os.getlogin())
elif enterValue == "c":
    path = str(input("Enter the path you want to scan: "))
    if os.path.exists(path):
        print("[*] Indexing your system...")
        savedFiles = dirAllFP(path)
    else:
        print("Could not find the directory")
        input("")
        sys.exit()
else:
    print("You did not select a valid option above")
    input("")
    sys.exit()

print("[*] Starting Engine...")

input("Ready to start scan, press enter to begin")

print("\n")

print("[*] Starting Scan...")

cursor.hide()
threts = []
for i in savedFiles:
    print("[*] Scanning " + str(savedFiles.index(i)) + "/" + str(len(savedFiles)), end='\r')
    if i != sys.argv[0].replace("/","\\"):
        if checkStrings(getStrings(i)):
            print("[!] Threat Detected: " + i)
            threts.append(i)
cursor.show()

if len(threts) > 0:
    print("Threts have been detected!")
    print("Writing them to the logs...")
    with open("RATScanner.log", "a") as f:
        f.write("RAT Scanner | v1.0.5.3 - Scan Log\n")
        f.write("------------Detections-----------\n")
        for i in threts:
            f.write("Location: " + i + "\n")
else:
    print("No threts detected!")
    with open("RATScanner.log", "a") as f:
        f.write("RAT Scanner | v1.0.5.3 - Scan Log\n")
        f.write("------------Detections-----------\n")
        f.write("None")

input("")

sys.exit()