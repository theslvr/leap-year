A = int(input())

if A % 100 == 0 and A % 400 != 0:
    print('Обычный')
elif A % 400 == 0 or A % 4 == 0:
    print('Високосный')
else:
    print('Обычный')
