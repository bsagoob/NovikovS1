import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('iris.csv')

combinations = [('sepal.length', 'sepal.width'),
('sepal.length', 'petal.length'),
('sepal.length', 'petal.width'),
('sepal.width', 'petal.length'),
('sepal.width', 'petal.width'),
('petal.length', 'petal.width')]

for x, y in combinations:
    fig = plt.figure()
    n=0
    i=1
    while n<6:
        axn = fig.add_subplot(6, 1, i)
        axn.scatter(data[x], data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        n+=1
        i+=1
    else:
        break

plt.show()
