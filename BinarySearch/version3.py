##corrected Book version play with computer
def binary_search(list, item):

    low = 0
    high = len(list)-1

    while low <= high:
        mid = (round((high-low+1)/2))+low
        guess = list[mid]

        print(guess)

        x = input()
        if x == "yes":
            return " "
        if x == "mas bajo":
            high = mid -1
        elif x == "mas alto":
            low = mid + 1


    print(" ")

my_list = list(range(1,101))

print (binary_search(my_list,5))
