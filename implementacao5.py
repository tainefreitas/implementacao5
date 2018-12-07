import sympy as sp
import numpy as np
def f(x):
    return 1/(x**2+1)

def f_2(x):
    return sp.sin(0.5*x**1/2)/x

#Questao 1, nro 15
x = sp.Symbol('x')
integral =  sp.integrate(f(x))
derivada_dupla = sp.diff(f(x), x, 2)

print integral
print derivada_dupla

#Trapezio Repetida

#1/3 de Simpson Repetida

#3/8 de Simpson Repetida

#Questao 2, nro 15
#Euler

#Runge-Kutta 2a ordem

#Runge-Kutta 4a ordem

#Questao 3, nro 5