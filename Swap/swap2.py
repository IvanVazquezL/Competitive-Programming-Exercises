#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap = 0
    arr = [x-1 for x in arr]
    dict = {value: i for i,value in enumerate(arr)}
    print(dict)


    for index,element in enumerate(arr):
        if element > index:
            newIndex = dict[index]
            arr[index], arr[newIndex] = arr[newIndex], arr[index]
            dict[element] = newIndex
            dict[index] = index
            swap += 1

    print(arr)
    print(swap)


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
