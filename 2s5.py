import math
# Ввод данных
input_data = input("Введите радиус окружности и сторону квадрата через пробел: ")

# Разделяем строку на части, преобразуем их в числа
radius_str, side_square_str = input_data.split()
radius = float(radius_str)
side_square = float(side_square_str)

# Вычисляем длину окружности, площадь круга и площадь квадрата
c = 2 * math.pi * radius
S_circle = math.pi * radius ** 2
S_square = side_square ** 2

# Вычисляем процент площади круга от площади квадрата
p = (area_circle / area_square) * 100

# Форматируем вывод с округлением до сотых
c_str = f"{circumference:.2f}"
p_str = f"{percentage:.2f}"

# Вывод результата в одном print()
print(f"Длина окружности равно {c_str}. Площадь круга составляет {p_str}% от площади квадрата.")
