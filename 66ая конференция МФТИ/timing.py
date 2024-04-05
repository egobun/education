import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.rcParams.update({'font.size': 12})

x = np.linspace(0.3852/0.002, 5000, 60000)
f1 = (0.002*x-0.3852)/192*2
x1 = [500,1000,1500,2000,2500,3000,3500,4000,4500,5000]
y1 = [0.6,1.2,2.93,3.4,4.65,5.95,6.3,7.42,9.1,9.71]
for i in range(len(y1)):
    y1[i] = y1[i] / 192*2
#plt.rc('grid', linestyle=':', color='grey', linewidth= 1 )plt.grid(which='major')
plt.legend(fontsize=14)
# указываем в аргументе label содержание легенды 
plt.plot(x, f1, '-b')
plt.scatter(x1, y1,color='red',s = 30)


plt.xlabel(r'$rate\:[\frac{об}{мин}]$', fontsize=12)
plt.ylabel(r'$\frac{timing}{sintablesize}$', fontsize=14)

plt.xlim([-10, 5100])
plt.ylim([-0.001, 0.11])
plt.title("Зависимость timing от rate")
# выводим легенду
plt.minorticks_on()

plt.grid(which='major')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.show()