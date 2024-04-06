#!/bin/env python

menu = ["Ginger","Shrewed","Tapest","Magoni"]

print("In today's menu, we have:\n")
for m in menu:
    print(m)

choice = input("Chose your item by pressing the item number:\n")

if int(choice) == 1:
    print("You have chosen Ginger")
elif int(choice) == 2:
    print("You have chosen Shrewed")
elif int(choice) == 3:
    print("You have chosen Tapest")
elif int(choice) == 4:
    print("You have chosen Magoni")
elif int(choice) > 4:
    print("You have not made any valid choice")
