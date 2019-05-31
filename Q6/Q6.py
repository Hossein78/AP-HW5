import sys
from math import cos
from math import pi
import time
import subprocess
import matplotlib.pyplot as plt  


def Pprime(n,x):
    return n/(x**2-1) * (x*P(n,x) - P(n-1,x))

def xi(i,n):
    epsilon = sys.float_info.epsilon
    xn = cos(pi*(i-0.25)/(n+0.5))
    while True:
        fxn = P(n,xn)
        Dfxn = Pprime(n,xn)
        xnn = xn - fxn/Dfxn
        if(abs(xnn-xn)<epsilon):
            return xn
        xn = xnn

def P(n,x):
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        return ((2*n-1)*x*P(n-1,x) - (n-1)*P(n-2,x))/n


def w(i,n):
    return 2/((1-xi(i,n)**2)*Pprime(n,xi(i,n))**2)

def f(x):
    return (x**3)/(x+1) * cos(x**2)

def integral(f,a,b,n):
    res = 0
    for i in range(1,n+1):
        res += ((b-a)/2)*w(i,n)*f(((b-a)/2)*xi(i,n)+((b+a)/2))
    return res

yc = []
yp = []


print('                         In Seconds')
print('_____________________________________________________________')
for i in range(1,20):
    t1 = time.time()
    integral(f,0,1,i)
    t2 = time.time()
    
    tc1 = time.time()
    subprocess.call(["IntegrateC++.exe", str(i)])
    tc2 = time.time()

    print ("{:2d}".format(i), '| C++:', "{:.15f}".format(tc2-tc1), '     Python:', "{:.15f}".format(t2-t1))

    yc.append(tc2-tc1)
    yp.append(t2-t1)
plt.plot(range(1,20),yp)
plt.plot(range(1,20),yc)
plt.xlabel('Degree of Polynomial')
plt.ylabel('Runtime (in s)')
plt.show()
