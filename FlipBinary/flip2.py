#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    flip = 4294967295

    return n ^ flip




if __name__ == '__main__':


    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        print(result)
