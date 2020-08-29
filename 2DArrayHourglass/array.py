#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # print(arr[0][0]," ",arr[0][1]," ",arr[0][2])
    # print("   ",arr[1][1])
    # print(arr[2][0]," ",arr[2][1]," ",arr[2][2])
    #
    # print(arr[a][b]," ",arr[a][b+1]," ",arr[a][b+2])
    # print("   ",arr[a+1][b+1])
    # print(arr[a+2][b]," ",arr[a+2][b+1]," ",arr[a+2][b+2])
    # print("")

    maxSum = []
    for a in range(4):
        for b in range(4):
            sum = arr[a][b] + arr[a][b+1] + arr[a][b+2] + arr[a+1][b+1] + arr[a+2][b] + arr[a+2][b+1] + arr[a+2][b+2]
            maxSum.append(sum)
            sum = 0

    return max(maxSum)


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)
