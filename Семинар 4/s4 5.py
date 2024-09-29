import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Считываем данные из файла BTC_data.csv
data = pd.read_csv('BTC_data.csv')

# Преобразуем столбец с датами в формат datetime
data['time'] = pd.to_datetime(data['time'])

# Создаем график
plt.figure(figsize=(12, 6))
plt.plot(data['time'], data['close'])
plt.title('Исторический график цены биткоина')
plt.xlabel('Дата')
plt.ylabel('Цена закрытия')
plt.xticks
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d-%m-%y'))

poly_degree = 3
poly_coeffs = np.polyfit(range(len(data)), data['close'], poly_degree)
poly = np.poly1d(poly_coeffs)
poly_values = poly(range(len(data)))

plt.plot(data['time'], poly_values, 'r', label=f'Аппроксимация полиномом {poly_degree} степени')

plt.show()
