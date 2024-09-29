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
    plt.figure()
    plt.scatter(data[x], data[y])
    plt.xlabel(x)
    plt.ylabel(y)

    A = np.vstack([data[x], np.ones(len(data))]).T
    m, c = np.linalg.lstsq(A, data[y], rcond=None)[0]
    
    plt.plot(data[x], m*data[x] + c, 'r')

    print(f'Для графика {x} от {y}: коэффициент наклона = {m}, коэффициент сдвига = {c}')


plt.show()
