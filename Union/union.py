englishNumber = input()
englishStudents = input()
frenchNumber = input()
frenchStudents = input()

e = set(englishStudents.split())
f = set(frenchStudents.split())
print (len(e.union(f)))
