# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:03:45 2019

@author: C-82
"""

import Meal

IO_breakfast = open("1早饭.txt","r")
IO_lunch = open("2午饭.txt","r")
IO_dinner= open("3晚饭.txt","r")
IO_night = open("4夜宵.txt","r")
list_breakfast = IO_breakfast.readlines()
list_lunch = IO_lunch.readlines()
list_dinner = IO_dinner.readlines()
list_night = IO_night.readlines()

print("\n\n\nSir,do you want to know which meal of today?")
key_word = input("1 releates to breakfast\n2 releates to lunch\n3 releates to dinner\n4 releates to night\nand that 0 means all of them:\n")
key_word = int(key_word)
if key_word == 1:
    print("It's really good,today your breakfast is:")
    print(Meal.Find(list_breakfast))
if key_word == 2:
    print("It's really good,today your lunch is:")
    print(Meal.Find(list_lunch))
if key_word == 3:
    print("It's really good,today your dinner is:")
    print(Meal.Find(list_dinner))
if key_word == 4:
    print("It's really good,today your night is:")
    print(Meal.Find(list_night))


IO_breakfast.close()
IO_lunch.close()
IO_dinner.close()
IO_night.close()

