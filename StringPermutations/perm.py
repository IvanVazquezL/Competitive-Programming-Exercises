#Global dictionary used to store the permutations
dictionary = dict()

def stringPermutation(word,lower,higher):
    #If lower has been incremented to the same value as higher
    if lower == higher:
        #Convert word list back to string
        newWord = ''.join(word)
        #Add the string to the dictionary as key and give it 0 as value
        dictionary[newWord] = 0
    else:
        #Loops from 0 to length of word
        for i in range(lower,higher+1):
            #Swaps characters
            word[lower], word[i] =  word[i], word[lower]
            #Recursion, increment lower
            stringPermutation(word,lower+1,higher)
            #Swap the characters back to their place
            word[lower], word[i] =  word[i], word[lower]

#Receives two strings as parameters
def checkPermutation(str1,str2):
    #Converts str1 into a list to manipulate it
    word = list(str1)
    #The list of str1 is sent to check its permutations
    stringPermutation(word,0,len(word)-1)
    #Check if the second string is in the dictionary of permutations
    if str2 in dictionary:
        print("Second string is a permutation of the First string")
    else:
        print("Second string is not a permutation of the First string")

checkPermutation("abc","bac")
