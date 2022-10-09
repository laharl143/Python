# Question:  Please write a function that calculates liquid volume in a sphere using the following formula. The radius r  is always 10, so consider making it a default parameter.

# You can then test your solution by passing 2 for h and you should get the expected output.

# Expected output:  4071.5040790523717

import math

def liquidVolume(h, r):
    v = ((4 * (math.pi) * (r*r*r) / 3) - (((math.pi) * (h*h) * (3 * r - h)) / 3 ))
    return v
print(liquidVolume(2, 10))  # 4071.5040790523717        #my sol'n 




from math import pi

def liquidVolume(h, r):
    v = ((4 * pi * (r**3) / 3) - ((pi * (h**2) * (3 * r - h)) / 3 ))
    return v
print(liquidVolume(2, 10))  # 4071.5040790523717        #answer key