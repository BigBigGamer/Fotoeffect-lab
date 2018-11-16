import numpy as np
import matplotlib.pyplot as plt 

def f(x): #x-- градусы
    p1 =-3.668*10**(7)
    p2=-9.329*10**(9)
    p3 =7.457*10**(14)
    f = p1*x**2 + p2*x + p3
    return f

x = np.arange(0,3500,10)
plt.plot(x,f(x)/10**14,'-k',lw = 3)
plt.grid(b=True, which='major', color='k', linestyle='-')
plt.ylabel('Частота, $10^{14}$ Гц.')
plt.xlabel('Градусы')
#print((f(3250)-f(3252))/10**14)
print((f(2382)-f(2198))/10**14)
print((f(1106)-f(556))/10**14)

#plt.savefig('graphs/grad',dpi=400)
plt.show()