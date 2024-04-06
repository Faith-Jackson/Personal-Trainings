#!/bin/env python

age = input("How old are you?:\n")
if  int(age) == 50:
    print("You are 50 years old")
    
elif int(age) > 50:
    print("You are older than 50 years old")

elif int(age) == 26:
    print("You are in between 25 to 50 years old") 
    
else:
    print("You are barely " + age + "years old")
