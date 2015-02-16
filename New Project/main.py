import random
import sys
import os

item_list = ['icho', 'chris', 'mima', 'tosho', 'niksun', 'svet']

print(item_list [2:5])

other_events = ['wash the car', 'buy a cat', 'walk the dog']

to_do_list = [item_list, other_events]
print(to_do_list)

print((to_do_list[1][1]))

item_list.append('Onion')
print(to_do_list)

item_list.insert(1,'Kiflin')
item_list.sort()
item_list.remove("icho")
print(to_do_list)

list_2 = item_list + other_events
print(len(list_2))
print(max(list_2))
print(min(list_2))