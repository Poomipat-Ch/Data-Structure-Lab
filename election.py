x = [i for i in input().split()]
vote = dict()
for i in x:
    vote[i] = vote.get(i,0) + 1
print(x)
print(set(x))