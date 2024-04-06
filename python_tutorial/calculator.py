#!/bin/env python

num1, operator, num2 = input('Input the two numbers you want to calculate:\n').split()

num1 = int(num1)
num2 = int(num2)

if operator == '+':
	print(f"{num1} plus {num2} is equal to {num1+num2}")

elif operator == '-':
	print(f"{num1} minus {num2} is equal to {num1-num2}")

elif operator == '*':
	print(f"{num1} times {num2} is equal to {num1*num2}")

elif operator == '/':
	print(f"{num1} divided by {num2} is equal to {num1/num2}")

elif operator == '%':
	print(f"{num1} percent of {num2} is equal to {num1%num2}")

