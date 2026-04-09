from math import *

hs = [0.001, 0.01, 0.1]

for h in hs:
    x = -pi
    while x <= pi:
        approx = (sin(x + h) - sin(x)) / h
        print(f"{x}  {approx} {cos(x)}")
        x += 0.001
    print(f"For h={h}")
    print("x  Approx Derivative  cos(x)")