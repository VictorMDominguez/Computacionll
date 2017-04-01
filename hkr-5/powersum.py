import sys
def suma( x,  b):
    if(x == 1 or x == 2 or x == 3):
        return x
    z = (int)(x**(1/b))
    return z + suma(z, b)
m = input()
n = input()
print suma(m, n)
