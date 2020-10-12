#Function receives a string as parameter
def unique(word):
    #All the characters of the string become keys of dictionary and their value is 0
    dictionary = dict.fromkeys(word,0)
    #If the length of the string is the same as the length of the dictionary
    #Then all characters are unique, if not the word has repeated characters
    return ("All characters are unique" if len(word) == len(dictionary) else "The characters are not unique")



print(unique("book"))

# def unique(word):
#     dictionary = dict.fromkeys(word,0)
#     if len(word) == len(dictionary):
#         return "All characters are unique"
#     else:
#         return "The characters are not unique"
