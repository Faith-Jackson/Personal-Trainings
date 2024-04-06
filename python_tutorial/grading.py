#!/bin/env python

age = eval(input("What is your age?:\n"))
if age < 5:
        print('You can\'t be in school yet')

# If age is 5 go to kindergarten
elif age == 5:
	print('Go to Kindergarten')

# Ages 6 through 17 goes to grades 1 to 12
elif (age >= 6) and (age <=17):
	grade = age - 5
	print(f'Go to {grade}')
	
# If age is greater than 17, say go through college
elif age > 17:
	print('Go to college')

else:
	print('There is no room for you')
