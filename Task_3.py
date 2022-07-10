print('Введите координаты точки(X и Y), отличные от 0')
print()
x = float(input('x =  '))
y = float(input('y =  '))
print()
if x > 0 and y > 0:
    print(f'x = {x}; y = {y} -> I четверть')
elif x < 0 and y > 0:
    print(f'x = {x}; y = {y} -> II четверть')
elif x < 0 and y < 0:
    print(f'x = {x}; y = {y} -> III четверть')
elif x > 0 and y < 0:
    print(f'x = {x}; y = {y} -> IV четверть')
else:
    if x == 0 or y == 0:
        print('Некорректный ввод данных')
print()