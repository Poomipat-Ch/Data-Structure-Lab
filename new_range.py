n = [float(i) for i in input('*** New Range ***\nEnter Input : ').split()]

sum = []
if len(n) > 2:
    while n[0] < n[1]:
        sum.append(round(n[0],3))
        n[0] += n[2]
elif len(n) > 1:
    while n[0] < n[1]:
        sum.append(round(n[0],3))
        n[0] += 1
else:
    x = 0.0
    while x < n[0]:
        sum.append(round(x,3))
        x += 1

print(tuple(sum))