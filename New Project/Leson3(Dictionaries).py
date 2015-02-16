import random
import sys
import os

super_hero = {"Natsu" : "Lusy",  "Levy" : "Gray",  "Juvia" :
              "Happy",  "Lily" : "Gajel"}
              
print(super_hero["Natsu"])

del super_hero["Levy"]
super_hero["Juvia"] = "Kana"

print(len(super_hero))
print(super_hero.get("Juvia"))

print(super_hero.keys())
print(super_hero.values())
