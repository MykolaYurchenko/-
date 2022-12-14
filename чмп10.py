import sympy as sp 
from math import factorial
def taylor(x):
    y=0
    d1 = sp.diff(f, x)
    d2 = sp.diff(d1, x)
    d3 = sp.diff(d2, x)
    print ('d1=', d1, 'd2=', d2, 'd3=', d3)
    y += f + d1*x + d2*(x-0)**2/factorial(2) +d3*(x-0)**3/factorial(3)
    print('y=', y)
    return y
x= sp.symbols('x')
f= 2.71**sp.sin(x)+2*x
taylor_x=taylor(x)
sp.plot(taylor_x, f, (x, -1, 1), label= 'Taylor')