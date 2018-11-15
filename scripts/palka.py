import numpy as np
from functions import parsing
import matplotlib.pyplot as plt 
name='rec\\n4.tsv'
f,I=parsing(name,1,2)

c=299792458 #м/с
e=1.60217662*10**(-19)# Кл
h = 6.62607004081*10**-34
pi=3.14159265
I=I/17
print(f[1])
x=np.array([f[1]-0.001,f[1],f[1]+0.001])
y=np.array([0,I[1],0])
plt.plot(x,y,'r')
print(f[0])
x=np.array([f[0]-0.001,f[0],f[0]+0.001])
y=np.array([0,I[0],0])
plt.plot(x,y,'r')
print(f[2])
x=np.array([f[2]-0.001,f[2],f[2]+0.001])
y=np.array([0,I[2],0])
plt.plot(x,y,'r')
print(f[3])
x=np.array([f[3]-0.001,f[3],f[3]+0.001])
y=np.array([0,I[3],0])
plt.plot(x,y,'r')
# plt.plot(f,I,'*')

plt.ylabel('I, отн.е.',fontsize=12) 
plt.xlabel('$\\nu,\\,$Гц',fontsize=12)# 
plt.grid()
plt.ylim((0, 1.1))
plt.savefig('palka.pdf')
plt.show()