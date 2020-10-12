def OneEdit(str1,str2):
    #Convert the strins into lists and then to sets
    set1 = set(list(str1))
    set2 = set(list(str2))
    #Subtract the sets
    setDifference = set1 - set2

    #If the difference is 1 or 0 elements, then it is one or 0 edits away
    #Else, it has more than one edit
    return("One or zero edits away" if len(setDifference) <= 1 else "More than one edit away")


print(OneEdit("pale","bale"))
