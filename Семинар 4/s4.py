import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0,1,2,3,4]
y = [0,1,4,9,16]


plt.figure(figsize=(8,5), dpi=100)

plt.plot(x,y, label='R1')

x2 = np.arange(0, 2.5, 0.05)

plt.plot(x2, x2**3, 'r', label='R2')

plt.title('R1,R2 U', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

plt.xlabel('t')
plt.ylabel('U')

plt.xticks([1.1,2.6,7.92])
plt.yticks([0,2.11,4.54,8.9])

plt.grid()

plt.legend()

plt.savefig('mygraph.png', dpi=300)

plt.show()
