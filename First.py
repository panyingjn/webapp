#！/usr/bin/env python3
#-*-coding:utf-8-*-

#y=ax*2+bx+c的解
import math
def quadratic(a,b,c):
    if not isinstance(a,b,c, int):
        raise TypeError('bad operand type')
    if (b**2-4*a*c)<0:
        print("no solution")
    elif (b**2-4*a*c)==0:
        x=-b/(2*a)
        return x
    else:
        x1 = ((-b+math.sqrt(b**2-4*a*c))/(2*a))
        x2 = ((-b -math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
        return x1,x2

