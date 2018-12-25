# 一个简单的回归

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# for regression
from numpy import polyfit
from numpy import polyval
import numpy as np

def normalize(data): # normalize the data
    rs = (data-data.mean())/data.std()
    return rs

data = pd.read_table(r'prices.txt',sep=',')

data['size'] = normalize(data['size'])

# start regression

x = data['size']
y = data['price']

def getModel(n,x,y):
    # parameters of poly
    parameter = polyfit(x, y, n)
    return parameter

def checkLost(p,x,y):
    yhat = polyval(p,x)
    print(abs(yhat-y).mean())

def showSeveralModels(nList,x,y):
    # x0 for drawing models
    x0 = np.linspace(-2, 4, 1000)
    plt.scatter(x,y)
    for i in nList:
        print(i)
        p = getModel(i,x,y)
        y0 = np.polyval(p, x0)
        plt.scatter(x0,y0,s=1)
        print(str(i)+":")
        checkLost(p,x,y)

    plt.show()

showSeveralModels([1,2,4,5],x,y)

