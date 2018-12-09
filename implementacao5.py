#TODO: Questao 2 e 3

from __future__ import division
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

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

def erro_trapezio(a,b,n):
    h=(b-a)/n
    temp=h**3
    e=(temp)/12
    g=[]
    aux=a
    i=1
    temp=0
    while(i<=n):
        temp=abs((sp.diff(f(x),x,2).subs(x,aux)))
        g.append(temp)
        aux=aux+h
        i=i+1
    #print(g)
    #print(max(g))
    temp=max(g)
    #print (e)
    e=e*temp
    return abs(e)

def erro_simpson13(a,b,n):
    h=(b-a)/n
    e=((h**4)/180)*(b-a)
    g=[]
    aux=a
    i=1
    temp=0
    while(i<=n):
        temp=abs((sp.diff(f(x),x,4).subs(x,aux)))
        g.append(temp)
        aux=aux+h
        i=i+1
    temp=max(g)
    e=e*temp
    return abs(e)

def erro_simpson38(a,b,n):
    h=(b-a)/n
    e=((h**4)/80)*(a-b)
    g=[]
    aux=a
    i=1
    temp=0
    while(i<=n):
        temp=abs((sp.diff(f(x),x,4).subs(x,aux)))
        g.append(temp)
        aux=aux+h
        i=i+1
    temp=max(g)
    e=e*temp
    return abs(e)
#Euler
#FIXME: Ei, de um jeito em mim!
def euler(x0, h, iteracoes):
    y0 = f_2(x0)
    intervaloX = [x0]
    intervaloY = [y0]
    intervaloYoriginal = [y0]
    
    for i in range (iteracoes):
        x1 = x0 + h
        intervaloX.append(x1)
        temp = sp.diff(f_2(x), x).subs(x,y0)
        y = y0 + h*temp
        intervaloY.append(y)
        intervaloYoriginal.append(f_2(x1))
        y0 = y
        x0 = x1
    
    plt.plot(intervaloX, intervaloYoriginal)
    plt.plot(intervaloX, intervaloY)
    plt.title("Questao 2 - Euler")
    plt.show()

#Questao 1, nro 15
x = sp.Symbol('x')

integral =  sp.integrate(f(x),(x,0,1))
#derivada_dupla = sp.diff(f(x), x, 2)

#Ao aumentar as particoes do intervalo, o erro tende a diminuir
print ("Valores das integrais usando:")

resultado1 = trapezio_repetida(0, 1, 4)
print ("Regra do Trapezio: %f" %resultado1)

resultado2 = simpson1_repetida(0, 1, 4)
print ("Regra de 1/3 de Simpson Repetida: %f" %resultado2)

resultado3 = simpson3_repetida(0, 1, 4)
print ("Regra de 3/8 de Simpson Repetida: %f" %resultado3)

print ("Implementacao do Sympy: %f" %integral)

print ("Erro das regras:")
erro1 = erro_trapezio(0,1,4)
print ("Regra do Trapezio: %f" %erro1)

erro2 = erro_simpson13(0,1,4)
print ("Regra de 1/3 de Simpson Repetida: %f" %erro2)

erro3 = erro_simpson38(0,1,4)
print ("Regra de 3/8 de Simpson Repetida: %f" %erro3)

#Questao 2, nro 15

euler(2, 0.4, 100)

#Runge-Kutta 2a ordem

#Runge-Kutta 4a ordem

#Questao 3, nro 5