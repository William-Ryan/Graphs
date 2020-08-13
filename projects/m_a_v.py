#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    
    arr.sort()
    #initiate value using the first two element
    min_dif = abs(arr[0] - arr[1])
    #go over the sorted list and compare the distance between neighbors
    for i in range(len(arr) - 1):
        dif = abs(arr[i] - arr[i + 1])
        if dif < min_dif:
            min_dif = dif
    return min_dif

array = [20, -15, -6, 120, -34] # = 9
print(minimumAbsoluteDifference(array))