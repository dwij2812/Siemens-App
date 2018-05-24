from matplotlib import pyplot as plt
from matplotlib import style
import numpy
from numpy import genfromtxt
import csv
import pandas as pd
from operator import itemgetter
from datetime import*
#######################################################################
values=[]
dates=[]
combine=[]
with open('test.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)
        values.append(row[0])
        dates.append(row[1])
        combine.append(row)
csvFile.close()
print(values)
print(dates)
print(combine)
print('The Number of Values are: ',len(values))
print('The Number of Dates are:',len(dates))
combine = sorted(combine, key=itemgetter(0))
for i in combine:
    print(i)
for i in combine:
    m2=i[0]
    m2=datetime.strptime(m2,'%m-%d-%Y %I:%M %p')
    i[0]=m2
combine = sorted(combine, key=itemgetter(0))
for i in combine:
    print(i)
