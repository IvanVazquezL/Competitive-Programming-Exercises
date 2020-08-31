#!/bin/python3

import math
import os
import random
import re
import sys

binary = []

def decimalToBinary(n):
    if n > 1:
        decimalToBinary(n//2)
    binary.append(n%2)

# Complete the flippingBits function below.
def flippingBits(n):
    string = ""
    decimalToBinary(n)

    array = [1] * (32-len(binary))

    for index,element in enumerate(binary):

        if element == 1:
            binary[index] = 0
        else:
            binary[index] = 1

    string = string.join([str(elem) for elem in binary])

    stringOnes= ""
    stringOnes = stringOnes.join([str(elem) for elem in array])

    fullBinary = stringOnes + string

    return int(fullBinary,2)



if __name__ == '__main__':


    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        binary = []

        print(result)
