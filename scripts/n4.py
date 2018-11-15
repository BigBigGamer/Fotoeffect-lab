import numpy as np
from functions import parsing
import matplotlib.pyplot as plt 
name='rec\\n4.tsv'
f,I=parsing(name,1,2)

c=299792458 #м/с
e=1.60217662*10**(-19)# Кл
h = 6.62607004081*10**-34
pi=3.14159265
print(f)
print()
nominalV=0.834 #Вольт/дел
nominaldV=0.0834

df=abs(f[0]-f[1])
print(df)
h=2*nominaldV*e/df
print(h)

df=abs(f[2]-f[3])
print(df)
h=0.375*e/df
print(h)
# #Возьмем первые две частоты

# plt.plot(f,I,'*')
# plt.show()