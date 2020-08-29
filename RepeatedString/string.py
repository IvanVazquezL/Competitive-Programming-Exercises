#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):

    if set(s) == {"a"} :
        return n
    elif set(s) == {"b"} :
        return 0
    else:
        length = len(s)
        repeat = s.count('a')

        if length == n:
            return repeat
        else:
            times = n/length

            if (times % 2) == 0:
                return int(times * repeat)
            else:
                partial = int(times) * repeat

                cut = n - (int(times) * length)

                return partial + s[:cut].count('a')



if __name__ == '__main__':
    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)
