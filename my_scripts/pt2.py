import numpy as np
import matplotlib.pyplot as plt 
import os

name='data\\pt2.txt'
os.chdir(os.path.dirname(__file__))
file = open(os.getcwd()+'\\'+name,'r')
data = file.readlines()
I = [float(s) for s in data[0].split('\t')]
Freq = [float(s) for s in data[1].split('\t')]

def f(x): #x-- градусы
    p1 =-3.668*10**(7)
    p2=-9.329*10**(9)
    p3 =7.457*10**(14)
    f = p1*x**2 + p2*x + p3
    return f

Freq = f(np. array(Freq)) / 10**14 
err = (f(3250)-f(3252))/10**14
plt.errorbar(Freq, I, xerr = err, yerr = 1, color = 'k')
plt.plot(Freq,I,'-ok',ms = 4)
plt.xlabel('Частота, $10^{14}$ Гц.')
plt.ylabel('Ток, мА')
plt.minorticks_on()
plt.grid(b=True, which='major', color='k', linestyle='-')
plt.grid(b=True, which='minor', color='b', linestyle='--')
plt.savefig('graphs/pt2',dpi=400)
plt.show()
