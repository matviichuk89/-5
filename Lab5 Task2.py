import math
Ax = float(input("Введіть координату точки A по осі X: "))
Ay = float(input("Введіть координату точки A по осі Y: "))
Bx = float(input("Введіть координату точки B по осі X: "))
By = float(input("Введіть координату точки B по осі Y: "))
Cx = float(input("Введіть координату точки C по осі X: "))
Cy = float(input("Введіть координату точки C по осі Y: "))
SA = abs(Ax) + abs(Ay)
SB = abs(Bx) + abs(By)
SC = abs(Cx) + abs(Cy)
if SA < SB and SC < SB:
    print("Точка B найбільша")
elif SB < SA and SC < SA:
    print("Точка A найбільша")
elif SA < SC and SB < SC:
    print("Точка C найбільша")
else:
    print("Декілька точок мають однакову найбільшу суму відстаней до осей OX і OY")