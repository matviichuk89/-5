import math
x=float(input("Введіть число: "))
if x>=5.2:
    y=math.exp(x)**3.27*abs(7-9)+1
    print("y =", y)
elif 0.19<x<5.2:
    y=math.cos(x)+math.cos(x)/math.sin(x)+math.sqrt(abs(x-7.84))
    print("y =", y)
else:
    y=math.sin(abs(x-0.7))+3.33*2**x
    print("y =", y)
