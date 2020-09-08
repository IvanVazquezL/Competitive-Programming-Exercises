#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    # dictAnagram = {}
    #
    # for element in s:
    #         if element in dictAnagram:
    #             dictAnagram[element] += 1
    #         else:
    #             dictAnagram[element] = 1
    #
    # if len(dictAnagram) == len(s):
    #     return 0
    # print(dictAnagram)
    dict={}

    count=0

    for i in range(len(s)):

        for j in range(i+1,len(s)+1):

            list1= list(s[i:j].strip())
            print(list1)

            list1.sort()
            print(list1)

            transf=''.join(list1)
            print(transf)


            if transf in dict:

                count+=dict[transf]

                dict[transf]=dict[transf]+1

            else:
                dict[transf]=1

            print(dict)
            print(count)
            print(" ")


    return count

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)
