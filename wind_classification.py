print(" *** Wind classification *** ")
n = float(input('Enter wind speed (km/h) : '))
wide = 'Breeze' if n < 52 else 'Depression' if n < 56 else 'Tropical Storm' if n < 102 else 'Typhoon' if n < 209 else 'Super Typhoon'
print('Wind classification is',wide+'.')