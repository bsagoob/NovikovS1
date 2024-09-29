import pandas as pd
import matplotlib.pyplot as plt

iris_data = pd.read_csv('iris.csv')

variety_distribution = iris_data['variety'].value_counts()

length_conditions = [
    iris_data['petal.length'] > 1.5,
    (iris_data['petal.length'] > 1.2) & (iris_data['petal.length'] <= 1.5),
    iris_data['petal.length'] <= 1.2
]

length_labels = ['> 1.5 cm', '1.2 cm < PetalLengthCm ≤ 1.5 cm', '≤ 1.2 cm']
length_distribution = [iris_data[cond].shape[0] for cond in length_conditions]

plt.figure(figsize=(16, 9))

plt.subplot(1, 2, 1)
plt.pie(variety_distribution, labels=variety_distribution.index,)
plt.title('Species')

plt.subplot(1, 2, 2)
plt.pie(length_distribution, labels=length_labels)
plt.title('PetalLengthCm')

plt.show()
