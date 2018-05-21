from matplotlib import pyplot as plt
from matplotlib import style
import numpy
from numpy import genfromtxt
data = genfromtxt('example.csv',delimiter=' ')
data=data[~numpy.isnan(data)]
print(data)
listobj=data.tolist()
print(listobj)
plt.plot(data)
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()
crossed=0
item=0
for i in listobj:
    item+=1
    if i>1100:
        print('Value Crossed')
        crossed+=1
    else:
        print('Value OK')
print('\n The Value Has Been crossed ',crossed,' Out of ',item,' no of times')
