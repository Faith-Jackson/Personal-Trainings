investment = input('Please enter your investment amount:\n')
interest = input('Please input your stipulated interest:\n')

investment = int(investment)
interest = float(interest)

earning = investment % interest

earning = float(earning)

for e in range(1, 10):
    yearly = e*earning
    print(f'Your interest for year {e} will be  {yearly:.2f}')
tenyears = earning*10
print(f'Your earning in 10 years will be {tenyears:.2f}')
