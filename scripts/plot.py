
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter 
from functions import parsing
import csv
import numpy as np
# def parsing(name,row1,row2):
# 	x=np.array([])
# 	y=np.array([])
# 	with open(name) as tsv:
# 	    reader = csv.reader(tsv, delimiter="\t")
# 	    for i in reader:
# 	        x=np.append(x,i[row1])
# 	        y=np.append(y,i[row2])
# 	x=np.asfarray(x,float)
# 	y=np.asfarray(y,float)
# 	return x,y

x,y=parsing('filters1.tsv',0,2)

plt.plot(x,y)
plt.title('Фазо-частотная характеристика',fontsize=16) 
plt.ylabel('$I_а$,мА',fontsize=16) 
plt.xlabel('$\\varphi_y$,В',fontsize=16) 
plt.grid () 
plt.plot(x,y,'ko',markersize=2) 
plt.plot(x,y)
# plt.xticks([i for i in range(0,10,1)]) # Х-сетка
# plt.yticks([i for i in range(0,10,1)]) # Y-сетка

# plt.errorbar(x, y, yerr=0.1) #Погрешности
# plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x))) #???
# plt.xlim([0,5]) # Пределы оси
# plt.ylim([0,5]) #
plt.savefig('filters1.pdf')
plt.show()

# Надписи
# plt.axvline(21.75,ymin=0, ymax=0.783,color='k', linestyle='--') 
#plt.text(21.6, -4,'$\\phi_1$') 
# plt.axvline(31,ymin=0, ymax=0.59,color='k', linestyle='--') 
# plt.text(31.2, -4,'$\\phi_{min}$') 
# plt.axvline(43,ymin=0, ymax=0.93,color='k', linestyle='--') 
# plt.text(43.2, -4,'$\\phi_2$') 