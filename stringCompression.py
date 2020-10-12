def stringCompression(stringRepeat):
    #initialize the counter for characters
    counter = 0
    #establish currentCharacter as the first character
    currentCharacter = stringRepeat[0]
    #initialize the new string
    compressed = ""
    #We will go through each character
    for i in stringRepeat:
         if currentCharacter is not i:
             #Add to the string the last character and their counter
             compressed += currentCharacter + str(counter)
             #The new character is now the currentCharacter
             currentCharacter = i
             #Reinitialize the counter
             counter = 0
             #Increment the counter in one for this first time
             counter += 1
         else:
             #Increment the counter
             counter += 1

    #Add to the string the last character and the last counter
    compressed += currentCharacter + str(counter)

    #If the new string is bigger than the original string, return the original
    return(stringRepeat if len(compressed) > len(stringRepeat) else compressed)


print(stringCompression("aabcccccaaa"))
