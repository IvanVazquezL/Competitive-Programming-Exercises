##Version 2 input and output with text files
contactList = []
file = open("sampleInput.txt", "r")

for name in file:
    name = name.strip('\n')
    contactList.append(name)

contactList.sort()

with open("outputVersion2.txt", "w") as newFile:
    for name in contactList:
        newFile.write(name+"\n")
