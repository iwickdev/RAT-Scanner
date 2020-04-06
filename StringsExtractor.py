import os
import sys
import easygui

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

filePath = easygui.fileopenbox()
if not os.path.exists(filePath):
    print("File selected does not exist!")
    input("")
    sys.exit()

strings = getStrings(filePath)
with open("StringDump.txt", "a") as f:
    for i in strings:
        f.write(i + "\n")