print('*** Fun with countdown ***')
x = [int(i) for i in input('Enter List : ').split()]
sum = []
countdown = []
countdowns = []
n = 0
for i in range(len(x)):
    if i != len(x)-1:
        n = x[i+1]  
    if x[i] == 1:
        countdown.append(1)
        countdowns.append(countdown)
        countdown = []
    elif x[i] - 1 == n:
        countdown.append(x[i])
    else:
        countdown = []
        
sum.append(len(countdowns))
sum.append(countdowns)
print(sum)