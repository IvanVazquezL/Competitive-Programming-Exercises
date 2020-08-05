## Version 1 read directly from the command prompt
contactList = []

name = input();
while name:
    contactList.append(name)
    name = input()

contactList.sort()

for name in contactList:
  print(name)
