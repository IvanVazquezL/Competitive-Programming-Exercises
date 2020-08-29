#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):

    firstArray = a[:int(d)]
    SecondArray = a[-(len(a)-int(d)):]

    newAlpha= SecondArray + firstArray

    return newAlpha

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
