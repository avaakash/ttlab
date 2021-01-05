side1, side2, side3 = map(int, input("Enter three sides: ").split())

if side1 == side2 == side3:
    print('Equilateral')
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles")
else:
    print("Scalene")