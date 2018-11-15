import numpy as np
from functions import parsing
import matplotlib.pyplot as plt 
name='rec\\n3.tsv'
l,V=parsing(name,0,1)

def f(x): #x-- градусы
    p1 =-3.668*10**(7)
    p2=-9.329*10**(9)
    p3 =7.457*10**(14)
    f = p1*x**2 + p2*x + p3
    return f


# plt.plot(l,V)
# plt.show()
x=f(l)
print(x)
plt.plot(f(l),V,'r.')
plt.ylabel('$V_з$,мА',fontsize=16) 
plt.xlabel('$\\nu, 10^{14}$Гц',fontsize=12)
# yerror=V*0.01
# # plt.errorbar(yerr=yerror) #Погрешности
# e=1.60217662*10**-19 #Кулона
# k= 8.307
# b= -25.26
# h=6.28*k*10**-6*e
# plt.plot(x,k*x+b)
# print('Постоянная Планка h=',h) #Херня конечно, но вдруг так и есть
# plt.grid() 
# plt.savefig('n3.pdf')
plt.show()