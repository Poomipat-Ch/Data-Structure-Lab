x = int(input('Enter Input : '))

for i in range(x + 1, -1, -1):
    print('.' * i + '#' * (x + 2 - i), end='')
    print('+' + ('+' * x if i == x + 1 or i == 0 else '#' * x) + '+')
for e in range(x+2):
    print('#' + ('#' * x if e == x + 1 or e == 0 else '+' * x) + '#', end='')
    print('+' * (x + 2 - e) + '.' * e)