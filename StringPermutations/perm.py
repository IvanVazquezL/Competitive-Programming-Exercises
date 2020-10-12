def stringPermutation(word,lower,higher):
    if lower == higher:
        print(word)
    else:
        for i in range(lower,higher):
            print(word)
            word[lower], word[i] =  word[i], word[lower]
            stringPermutation(word,lower+1,higher)
            word[lower], word[i] =  word[i], word[lower]




word = list("abc")
stringPermutation(word,0,len(word)-1)
