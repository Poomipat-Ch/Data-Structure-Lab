print("*** Converting hh.mm.ss to seconds ***")
n = input('Enter hh mm ss : ')
h, m, s = map(int,n.split())

if 0 <= h <= 24 and 0 <= m <= 59 and 0 <= s <= 59:
    print(f'{h:02d}:{m:02d}:{s:02d} = {((h*3600)+(m*60)+s):,} seconds')
elif m < 0 or m > 59:
    print(f'mm({m}) is invalid!')
else:
    print(f'ss({s}) is invalid!')