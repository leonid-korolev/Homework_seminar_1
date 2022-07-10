print('Введите цифру, обозначающую день недели')
d = float(input())
if  d == int(d):
    if  6 <= d < 8:
        print(f'{round(d)} -> ДА')
    elif d >= 1 and d < 6:
        print(f'{round(d)} -> Нет')
    elif d < 1 or d > 7: 
        print(f'{round(d)} -> Это не день недели') 
else:
    print('Введите целое число')
