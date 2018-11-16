import numpy as np
import matplotlib.pyplot as plt 
import os

def f(x): #x-- градусы
    p1 =-3.668*10**(7)
    p2=-9.329*10**(9)
    p3 =7.457*10**(14)
    f = p1*x**2 + p2*x + p3
    return f
e = 1.60217733*10**(-19)
name='data\\pt3.txt'
os.chdir(os.path.dirname(__file__))
file = open(os.getcwd()+'\\'+name,'r')
data = file.readlines()
V = [float(s) for s in data[0].split('\t')]
Freq = [float(s) for s in data[1].split('\t')]
Freq = f(np. array(Freq)) 

m,k = np.polyfit(Freq,V,1)
print(m,k)
print(m*e*0.95)
print(-k/m/10**14)
err = (f(3250)-f(3252))
plt.errorbar(Freq, V, xerr = err, yerr = 0.1*0.25, color = 'k',linestyle = '')
plt.plot(Freq,Freq*m + k,'-r')
plt.plot(Freq,V,'ok',ms = 4)
plt.xlabel('Частота, $10^{14}$ Гц.')
plt.ylabel('$V_{3},В$')
plt.minorticks_on()
plt.grid(b=True, which='major', color='k', linestyle='-')
#plt.savefig('graphs/pt3',dpi=400)
plt.show()