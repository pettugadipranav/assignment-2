import math
from fractions import Fraction as frac

x = 1
a = frac(1, 2) * math.acos(frac((1 - x), (1 + x)))
b = math.atan(math.sqrt(x))
if (a == b):
    print("yes")
else:
    print("no")

