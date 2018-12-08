#TODO: Questao 1, 2 e 3
#TODO: Erros 1

import sympy as sp
import numpy as np

def f(x):
    return 1/(x**2+1)

def f_2(x):
    return sp.sin(0.5*x**1/2)/x

#Regra do Trapezio Repetida
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

#Regra de 1/3 de Simpson Repetida
def simpson1_repetida (a, b, particoes):
    h = (b-a)/particoes
    y = [f(a)]
    xn = a
    for i in range (particoes-1):
        x = xn + h
        if ((i+1)%2 == 0):
            aux = 2*f(x)
        else:
            aux = 4*f(x)
        y.append(aux)

    y.append(f(b))
    resultado = h/3 * sum(y)
    return resultado

#Regra 3/8 de Simpson Repetida
def simpson3_repetida (a, b, particoes):
    h = (b-a)/particoes
    y = [f(a)]
    xn = a
    for i in range (particoes-1):
        x = xn + h
        if ((i+1)%3 == 0):
            aux = 2*f(x)
        else:
            aux = 3*f(x)
        y.append(aux)

    y.append(f(b))
    resultado = (3/8)*h * sum(y)
    return resultado

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
x = sp.Symbol('x')
integral =  sp.integrate(f(x),(x,0,1))
#derivada_dupla = sp.diff(f(x), x, 2)

print ("Valores das integrais usando:")

resultado1 = trapezio_repetida(0, 1, 4)
print ("Regra do Trapezio:", resultado1)

resultado2 = simpson1_repetida(0, 1, 4)
print ("Regra de 1/3 de Simpson Repetida:", resultado2)

resultado3 = simpson3_repetida(0, 1, 4)
print ("Regra de 3/8 de Simpson Repetida:", resultado3)

print ("Implementacao do Sympy:", integral)

print ("Erro das regras:")
erro1 = 0
print ("Regra do Trapezio:", erro1)

erro2 = 0
print ("Regra de 1/3 de Simpson Repetida:", erro2)

erro3 = 0
print ("Regra de 3/8 de Simpson Repetida:",erro3)

#Questao 2, nro 15
#Euler


#Runge-Kutta 2a ordem

#Runge-Kutta 4a ordem

#Questao 3, nro 5