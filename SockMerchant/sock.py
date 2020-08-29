#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dic = {}
    pairs = 0

    for x in ar:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1

    for value in dic.values():
        pairs += int(value/2)

    return pairs

if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
