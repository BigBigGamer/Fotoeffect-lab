import numpy as np
import matplotlib.pyplot as plt 
import os
import scipy as sp

name='data\\2500.txt'
os.chdir(os.path.dirname(__file__))
file = open(os.getcwd()+'\\'+name,'r')
data = file.readlines()
F = [float(s) for s in data[0].split('\t')]
I = [float(s) for s in data[1].split('\t')]
m,k = np.polyfit(I,F,1)

plt.figure(figsize=(9*1.5, 3.5*1.5))
plt.plot(I,np.array(I) * 0.96*m ,'r')
plt.plot(I,F,'ok')
plt.xlabel('Интенсивность, у.е.')
plt.ylabel('Фототок, мА')
plt.grid()
slope, intercept, r_value, p_value, std_err = sp.stats.linregress(I,F)
print(r_value)
#plt.savefig('graphs/2500',dpi=400)
plt.show()
