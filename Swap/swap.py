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

    for index,element in enumerate(arr):
        if element > index:
            newIndex = arr.index(index)
            arr[index], arr[newIndex] = arr[newIndex], arr[index]
            swap += 1

    print(arr)
    print(swap)


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
