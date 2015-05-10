import random
import sys
import os

def palindrome(obj):
    ls = []
    if type(obj) == str:
        for i in range(0, len(obj)):
            ls.append(obj[i])
    elif type(obj) == int:
        while obj > 0:
            ls.append(int(obj % 10))
            obj /= 10
    else:
        print ("Error!")
        return False
    length = len(ls)
    for i in range(0, length // 2):
        if ls[i] != ls[length - i - 1]:
            return False
    return True
    print('palindrome'(321))
    
