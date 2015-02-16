import random
import sys
import os

for x in range(0, 10):
    print(x, " ", end="")
    
hero_list = ['Natsu', 'Gray', 'Lusy', 'Happy']

for a in hero_list:
    print(a)
    
for b in [4,5,6,9,5,8,5,6,8]:
    print(b)
    
num_list = [[20,30,10],[1,2,3],[856,456,125]]

for a in range(0, 3):
    for b in range(0, 3):
        print(num_list[a][b])
