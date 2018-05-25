from matplotlib import pyplot as plt
from matplotlib import style
import numpy
from numpy import genfromtxt
import csv
import pandas as pd
from operator import itemgetter
from datetime import*
#######################################################################
def nearest(items, pivot):
    return min(items, key=lambda x: abs(x - pivot))
#######################################################################
values=[]
dates=[]
combine=[]
with open('test.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        values.append(row[1])
        dates.append(row[1])
        combine.append(row)
csvFile.close()
#print(values)
#print(dates)
#print(combine)
print('The Number of Values are: ',len(values))
print('The Number of Dates are:',len(dates))
combine = sorted(combine, key=itemgetter(0))
"""for i in combine:
    print(i)"""
for i in combine:
    m2=i[0]
    m2=datetime.strptime(m2,'%m-%d-%Y %I:%M %p')
    i[0]=m2
combine = sorted(combine, key=itemgetter(0))
"""for i in combine:
    print(i)"""
ref_min=combine[0][0].date()
min_time=datetime.strptime('0000','%H%M').time()
ref_min=datetime.combine(ref_min, min_time)
print(type(ref_min))
ref_max=combine[-1][0].date()
max_time=datetime.strptime('2359','%H%M').time()
ref_max=datetime.combine(ref_max, max_time)
print(ref_max)
ref_max+= timedelta(days=1)
dates=[]
for i in combine:
    dates.append(i[0])
i=ref_min
indices=[]
while i<ref_max:
    k=nearest(dates,i)
    print('The corresponding Lowest time related to this reading is: ',k)
    index=dates.index(k)
    print(index)
    indices.append(index)
    i += timedelta(days=1)
    print(i)
print('The Number of Indices are: ',len(indices))
k=ref_min.date()
for i in range(len(indices)-1):
    r_min=float(values[indices[i]])
    r_up=float(values[indices[i+1]])
    consumption=r_up-r_min
    print('The Consumption on ',k,' is : ',consumption)
    k+= timedelta(days=1)
