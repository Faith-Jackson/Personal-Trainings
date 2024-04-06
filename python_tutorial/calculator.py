num1, placement, num2 = input("Please input two numbers that you want to calculate.\nPlease use the following signs x,-,%,/,+\n:").split()

num1 = int(num1)
num2 = int(num2)

if placement == 'x':
    print(f"{num1} multiplied by {num2} is equal to {num1*num2}")

elif placement == '+':
    print(f"{num1} plus {num2} is equal to {num1+num2}")

elif placement == '-':
    print(f"{num1} minus {num2} is equal to {num1-num2}")

elif placement == '/':
    print(f"{num1} divided by {num2} is equal to {num1/num2}")

elif placement == '%':
    print(f"{num1} percent of {num2} is equal to {num1%num2}")

else:
    print("You have not used any valid placement")