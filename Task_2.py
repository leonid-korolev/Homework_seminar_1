print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
print()
print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x,y,z)
            print((int(not (x or y or z))) == (not x and not y and not z)) 
