from math import *

h = 0.001
x_start = -pi
x_end = pi
x = x_start

print("x\t\tApprox Derivative\tcos(x)\t\tDifference")
print("-" * 60)

count = 0
while x <= x_end + 0.000001: 
    if count % 200 == 0:
        approx_deriv = (sin(x + h) - sin(x)) / h
        cos_x = cos(x)
        difference = abs(approx_deriv - cos_x)
        
        print(f"{x:.4f}\t\t{approx_deriv:.6f}\t\t{cos_x:.6f}\t\t{difference:.8f}")
    
    x += 0.001
    count += 1

print("\nTask completed for h =", h)