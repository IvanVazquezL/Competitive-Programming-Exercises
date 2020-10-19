#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    #Counter of triplets
    count = 0
    dict = {}
    dictPairs = {}

    #Looping through the array backwards
    for i in reversed(arr):
        #If i*r is in the dictPairs
        if i*r in dictPairs:
            #Increment the counter with the value of
            #i*r in dictPairs
            count += dictPairs[i*r]
        #If i*r is in dict
        if i*r in dict:
            #Insert i in dictPairs giving it the value of
            #dictPairs[i] plus dict[i*r]
            dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]

        #Insert i in dict, giving it the value of dict[i] plus one
        dict[i] = dict.get(i, 0) + 1

    return count

if __name__ == '__main__':

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)
