import math
print('Введите координаты точки А')
X1 = float(input('X1 = '))
Y1 = float(input('Y1 = '))
print('Введите координаты точки B')
X2 = float(input('X2 = '))
Y2 = float(input('Y2 = '))
print()
AB = round(math.sqrt((X2-X1)**2 + (Y2-Y1)**2),2)
print(f'A({X1},{Y1}); B({X2},{Y2}) -> {AB}') 
print()