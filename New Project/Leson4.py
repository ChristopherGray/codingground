import random
import sys
import os

age = 30
if age > 16:
    print("You are old enough to drive")
else:
    print("You are not")
    
if age >= 21:
    print("You are old enough to drive a car")
elif age >=16:
    print("You are old enough to drive")
else:
    print("You are not")
    
if((age >= 1) and (age <= 18)):
    print("You are awsome")
elif ((age==21) or (age<=65)):
    print("You are awsome")

elif not(age == 30):
    print("You are not awsome")
else:
    print("You get a party")
