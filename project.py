A = int(input())

if A % 100 == 0 and A % 400 != 0:
    print('usual')
elif A % 400 == 0 or A % 4 == 0:
    print('leap')
else:
    print('usual')
