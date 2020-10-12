#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    maxNumber = max(arr)
    dictNumbers = dict.fromkeys(arr,0)
    newList = []
    newList.append(1)

    for number in dictNumbers:
        if number is not maxNumber:
            newList.append(number*r)

    tripleList = []
    triple = []

    for i=0; i<=(len(newList)-3); i++:
        for a=i; a<=(a+3);a++:
            triple.append(newList[a])
        tripleList.append(triple)
        triple = []


    print(newList)

if __name__ == '__main__':
    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)
