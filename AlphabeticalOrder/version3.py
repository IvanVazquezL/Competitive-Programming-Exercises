##Version 3 solution without the sort function
contactList = []
file = open("sampleInput.txt", "r")

for name in file:
    name = name.strip('\n')
    contactList.append(name)

for i in range(len(contactList)):
    for j in range(i + 1, len(contactList)):

        if contactList[i] > contactList[j]:
           contactList[i], contactList[j] = contactList[j], contactList[i]

with open("outputVersion3.txt", "w") as newFile:
    for name in contactList:
        newFile.write(name+"\n")
