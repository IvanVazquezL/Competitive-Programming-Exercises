#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    arr=[]
    ans=[]
    dictionary={}
    for query in queries:
        for j in range(1):
            if query[0]==1:
                arr.append(query[1])
                dictionary[query[1]] = dictionary.get(query[1],0) + 1
            elif query[0]==2:
                try:
                    arr.remove(query[1])
                except:
                    break
            else:
                if query[1] in dictionary.values():
                    ans.append(1)
                else:
                    ans.append(0)


    return ans




if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print(ans)
