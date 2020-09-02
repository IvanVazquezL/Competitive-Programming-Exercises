#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
  dictString1 = dict.fromkeys(s1,0)
  dictString2 = dict.fromkeys(s2,0)
  dict3 = {**dictString1, **dictString2}

  if len(dict3) < len(dictString1)+ len(dictString2):
    return "YES"
  else:
    return "NO"

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result)
