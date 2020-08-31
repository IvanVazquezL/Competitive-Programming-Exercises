#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    dictMagazine = {}
    dictNote = {}

    for element in magazine:
            if element in dictMagazine:
                dictMagazine[element] += 1
            else:
                dictMagazine[element] = 1

    for element in note:
            if element in dictNote:
                dictNote[element] += 1
            else:
                dictNote[element] = 1

    allWords = 0

    for element in note:
        if element in dictMagazine:
            numberMagazine = dictMagazine[element]
            numberNote = dictNote[element]

            if numberMagazine-numberNote >= 0 :
                allWords += 1
            else:
                return "No"
        else:
            return "No"

    if allWords == len(note):
        return "Yes"

    print(dictMagazine)
    print(dictNote)

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
