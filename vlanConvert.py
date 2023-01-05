#imports regex
from os import name
import re

#function to remove default vlans
def defaultVlanRemoval(numList, nameList):
    #removes vlan 1
    if "1   " in numList:
        numList.remove("1   ")
        if "default                          " in nameList:
            nameList.remove("default                          ")
        else:
            print("VLAN 1 REMOVAL FAILURE")
    else:
        print("VLAN 1 not found, continuing...")
    
    #removes vlan 1002
    if "1002" in numList:
        numList.remove("1002")
        if "fddi-default                     " in nameList:
            nameList.remove("fddi-default                     ")
        else:
            print("VLAN 1002 REMOVAL FAILURE")
    else:
        print("VLAN 1002 not found, continuing...")

    #removes vlan 1003
    if "1003" in numList:
        numList.remove("1003")
        if "trcrf-default                    " in nameList:
            nameList.remove("trcrf-default                    ")
        elif "token-ring-default               " in nameList:
            nameList.remove("token-ring-default               ")
        else:
            print("VLAN 1003 REMOVAL FAILURE")
    else:
        print("VLAN 1003 not found, continuing...")

    #removes vlan 1004
    if "1004" in numList:
        numList.remove("1004")
        if "fddinet-default                  " in nameList:
            nameList.remove("fddinet-default                  ")
        else:
            print("VLAN 1004 REMOVAL FAILURE")
    else:
        print("VLAN 1004 not found, continuing...")

    #removes vlan 1005
    if "1005" in numList:
        numList.remove("1005")
        if "trbrf-default                    " in nameList:
            nameList.remove("trbrf-default                    ")
        elif "trnet-default                    " in nameList:
            nameList.remove("trnet-default                    ")
        else:
            print("VLAN 1005 REMOVAL FAILURE")
    else:
        print("VLAN 1005 not found, continuing...")

#opens sh vlan br text file and puts it in var vlanBr
with open("vlanbrief.txt") as f:
    vlanBr = f.read()
print("file read successfully")

#splits vlanBr into list based on newlines
vlanBr = vlanBr.split("\n")

#variable declaration
search1 = r'^\d'
vlanNum = []
vlanName = []
vlanconfig = []

#takes vlan number and name from vlanBr
for line in vlanBr:
    if re.search(search1, line):
        vlanNum.append(line[0:4])
        vlanName.append(line[5:38])
print("vlanNum and vlanName created successfully")

#removes unnecessary vlans

defaultVlanRemoval(vlanNum, vlanName)

print("unecessary vlans removed")

#adds vlan and name commands to beginning of each item
for line in vlanNum:
    vlanNum[vlanNum.index(line)] = "vlan " + line
for line in vlanName:
    vlanName[vlanName.index(line)] = "name " + line
print("vlan and name commands added")

#combines vlanNum and vlanName
i = 0
for line in vlanName:
    vlanconfig.append(vlanNum[i])
    vlanconfig.append(vlanName[i])
    i += 1
print("VLAN config created")

#vlanconfig joined into string
vlanconfig = "\n".join(vlanconfig)

while " \n" in vlanconfig:
    vlanconfig = vlanconfig.replace(" \n", "\n")

#writes string to file
x = open("vlanconfig.txt", "w")
x.write(vlanconfig)
x.close
print("VLAN config written successfully to file")