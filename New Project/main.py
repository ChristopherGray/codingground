import random
import sys
import os
import math

def fibonachi(n):
    result = []
    for i in range(0, n):
        if i < 2:
            result.append(1)
        else:
            result.append(result[i - 1] + result[i - 2])
    return result
    
print(fibonachi(100))
