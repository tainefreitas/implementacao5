#TODO: Questao 1, 2 e 3

import sympy as sp
import numpy as np

def f(x):
    return 1/(x**2+1)

def f_2(x):
    return sp.sin(0.5*x**1/2)/x

def trapezio_repetida(a, b, particoes):
    h = (b-a)/particoes
    y = [f(a)]
    xn = a
    for i in range (particoes-1):
        x = xn + h
        aux = 2*f(x)
        y.append(aux)
        xn =  x
    y.append(f(b))

    resultado = h/2 * sum(y)
    return resultado

#def simpson1_3 (a, b, interacoes):


#FIXME: EDO de f(x, y)
def euler(x0, h, interacoes):
    y0 = f_2(x0)
    intervaloX = [x0]
    intervaloY = [y0]
    
    for i in range (interacoes):
        x = x0 + h
        intervaloX.append(x)
        x0 = x
        y = y0 + h*f_2(y0)
        intervaloY.append(y)
        y0 = y
    

#Questao 1, nro 15
#x = sp.Symbol('x')
#integral =  sp.integrate(f(x))
#derivada_dupla = sp.diff(f(x), x, 2)


#Trapezio Repetida

resultado1 = trapezio_repetida(0, 1, 4)
print (resultado1)

#1/3 de Simpson Repetida

#3/8 de Simpson Repetida

#Questao 2, nro 15
#Euler

#Runge-Kutta 2a ordem

#Runge-Kutta 4a ordem

#Questao 3, nro 5