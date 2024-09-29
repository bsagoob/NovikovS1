import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize = (16,9)) 
ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412) 
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)

values1 = np.random.normal(0, 10, 100)

ax1.hist(values1, 100)
ax1.grid()

ax1.set_title('100')

values2 = np.random.normal(0, 10, 1000)

ax2.hist(values2,100)
ax2.grid() 

ax2.set_title('1000')

values3 = np.random.normal(0, 10, 5000)

ax3.hist(values3, 100)
ax3.grid() 

ax3.set_title('5000')

values4 = np.random.normal(0, 10, 10000)

ax4.hist(values4, 100)
ax4.grid() 

ax4.set_title('10000')

plt.show()
