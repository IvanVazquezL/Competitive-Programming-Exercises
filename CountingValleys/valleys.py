#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    walk = [0]
    counter = 0
    valleys = 0

    for x in s:
        if x=="D" :
            if counter==0 :
                valleys += 1

            counter += -1
            walk.append(counter)

        else:
            counter += 1
            walk.append(counter)

    return valleys



if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)
