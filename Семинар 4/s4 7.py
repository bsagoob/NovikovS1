from collections import Counter
import re
import pandas as pd

# Шаг 1: Открыть и прочитать файл
data = pd.read_csv('agreement.txt')

# Шаг 2: Преобразовать текст в список слов
# Удаляем все символы кроме букв и пробелов, и приводим к нижнему регистру
words = re.findall(r'\b\w+\b', text.lower())

# Шаг 3: Подсчитать количество вхождений каждого слова
word_count = Counter(words)

# Шаг 4: Отсортировать слова по частоте и выбрать 10 самых частых
most_common_words = word_count.most_common(10)

# Шаг 5: Вывести результат
for word, count in most_common_words:
    print(f'{word}: {count}')
