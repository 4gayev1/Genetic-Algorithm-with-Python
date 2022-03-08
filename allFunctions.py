import numpy as np
from numpy import *

#Ackley

def ackley(x, y):
 func=-20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2)))-exp(0.5 * (cos(2 * pi * x)+cos(2 * pi * y))) + e + 20
 print("Ackley:", func)

x,y = -32.768, 32.768
ackley(x, y)


#Rastrigin

def rastrigin(X,Y):
    func = (X ** 2 - 10 * np.cos(2 * np.pi * X)) + \
        (Y ** 2 - 10 * np.cos(2 * np.pi * Y)) + 20
    result = sum(func) / len(func)
    print("Rastrigin:", result)
    return result

X = linspace(-32.768, 32.768)
Y = linspace(-32.768, 32.768)
rastrigin(X, Y)

#Rosenbrock

def rosenbrock(x1, x2):
    func=100*(x2-x1**2)**2+(x1-1)**2
    result = sum(func) / len(func)
    print("Rosenbrock:", result)

x1 = linspace(-32.768, 32.768)
x2 = linspace(-32.768, 32.768)

rosenbrock(x1, x2)

#Schwefel

def schwefel(x1, x2):
    cem=0
    func =418.9829*2 - x1 * sin(sqrt(abs(x1)))-x2*sin(sqrt(abs(x2)))
    for i in func:
        cem += sum(i)
    result = cem / len(func)
    print("Schwefel:", result)

    return 418.9829*2 - x1 * sin(sqrt(abs(x1)))-x2*sin(sqrt(abs(x2)))

x1=linspace(-32.768, 32.768)
x2=linspace(-32.768, 32.768)

schwefel(x1, x2)