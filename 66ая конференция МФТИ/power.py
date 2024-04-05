import numpy as np
import matplotlib.pyplot as plt
import matplotlib


matplotlib.rcParams.update({'font.size': 12})

x = np.linspace(100, 5000, 60000)
f1 = (0.0334*x+16)/2
x1 = [500,1000,1500,2000,2500,3000,3500,4000,4500,5000]
y1 = [20,33.5,42.1,55.6,71.4,76.3,95.2,105,110.15,135]
for i in range(len(y1)):
    y1[i] = y1[i]*0.75
#plt.rc('grid', linestyle=':', color='grey', linewidth= 1 )plt.grid(which='major')
plt.legend(fontsize=14)
# указываем в аргументе label содержание легенды 
plt.plot(x, f1, '-b')
plt.scatter(x1, y1,color='red',s = 30)


plt.xlabel(r'$rate\:[\frac{об}{мин}]$', fontsize=12)
plt.ylabel(r"power  [%]", fontsize=14)

plt.xlim([-10, 5100])
#plt.ylim([-0.001, 0.06])
plt.title("Зависимость power от rate")
# выводим легенду
plt.minorticks_on()

plt.grid(which='major')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
plt.show()