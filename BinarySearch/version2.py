##corrected Book version
def binary_search(list, item):
    print(" ")
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (round((high-low)/2))+low
        guess = list[mid]
        print("item:",item)
        print("low:",low)
        print("high:",high)
        print("mid:",mid)
        print("guess:",guess)
        print(" ")

        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1

    return None
    print(" ")

my_list = list(range(1,11))

print (binary_search(my_list,6))
