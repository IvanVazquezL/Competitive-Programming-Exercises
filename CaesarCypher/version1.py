alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
text = input()
shift = input()

firstArray = alpha[:int(shift)]
SecondArray = alpha[-(len(alpha)-int(shift)):]

newAlpha= SecondArray + firstArray

print(newAlpha)

newText = ""

for x in text:
    if x == " ":
        newText += x
    elif x == ",":
        newText += x
    elif x == ".":
        newText += x
    elif x == "!":
        newText += x
    elif x.isupper():
        newText += newAlpha[alpha.index(x.lower())].upper()
    else:
        newText += newAlpha[alpha.index(x)]

print(newText)
