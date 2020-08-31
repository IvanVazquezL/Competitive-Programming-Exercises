#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q,n):
    # rest = []
    # for x in range(n-1):
    #     rest.append(q[x]-q[x+1])
    #
    # print(rest)
    # positive = [b for b in rest if b >= 0 ]
    #
    # print(positive)
    #
    # for c in positive:
    #     if c > 2:
    #         return "Too chaotic"
    #
    # return sum(positive)
    #
    #########
    # change = []
    # for x in range(n):
    #     change.append((q[x]-1)-x)
    #
    # sum = 0
    # for x in range(len(change)):
    #
    #     if change[x]>0:
    #         if change[x]>2:
    #             return "Too chaotic"
    #         else:
    #             sum += change[x]
    #     elif change[x] < -1:
    #         sum += 1
    #    return sum
    ####################
    # change = []
    # for x in range(n):
    #     change.append((q[x]-1)-x)
    #
    # # print(change)
    #
    # for c in change:
    #     if c > 2:
    #      return "Too chaotic"

    bribe = 0

    for a in range(len(q)):
        if ((q[a]-1)-a) > 2:
            return "Too chaotic"

        c=a+1
        for b in range(len(q)-c):
            print(q[a]," > ", q[c+b])
            if q[a] > q[c+b]:
                bribe += 1


    print(bribe)




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q,n)


# 9
# 8
# 1 2 3 5 4 6 7 8
# 5
# 2 1 5 3 4
# 5
# 2 5 1 3 4
# 5
# 2 1 5 4 3
# 8
# 1 2 5 3 4 7 8 6
# 5
# 2 1 5 3 4
# 5
# 2 5 1 3 4
# 8
# 5 1 2 3 7 8 6 4
# 8
# 1 2 5 3 7 8 6 4
#
# 9
# 8
# 1 2 3 5 4 6 7 8
# [0, 0, 0, 1, -1, 0, 0, 0]
# Moves:  1
#
# 5
# 2 1 5 3 4
# [1, -1, 2, -1, -1]
# Moves:  3
#
# 5
# 2 5 1 3 4
# [1, 3, -2, -1, -1]
# Moves:  Too chaotic
#
# 5
# 2 1 5 4 3
# [1, -1, 2, 0, -2]
# Moves:  4
#
# 8
# 1 2 5 3 4 7 8 6
# [0, 0, 2, -1, -1, 1, 1, -2]
# Moves:  5
#
# 5
# 2 1 5 3 4
# [1, -1, 2, -1, -1]
# Moves:  3
#
# 5
# 2 5 1 3 4
# [1, 3, -2, -1, -1]
# Moves:  Too chaotic
#
# 8
# 5 1 2 3 7 8 6 4
# [4, -1, -1, -1, 2, 2, -1, -4]
# Moves:  Too chaotic
#
# 8
# 1 2 5 3 7 8 6 4
# [0, 0, 2, -1, 2, 2, -1, -4]
# Moves:  7

# def minimumBribes(q,n):
#     change = []
#     for x in range(n):
#         change.append((q[x]-1)-x)
#
#     for c in change:
#         if c > 2:
#          return "Too chaotic"
#
#     bribe = 0
#
#     for a in range(len(q)):
#         c=a+1
#         for b in range(len(q)-c):
#             if q[a] > q[c+b]:
#                 bribe += 1
#
#     return(bribe)
