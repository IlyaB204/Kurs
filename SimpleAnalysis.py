import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

random_num = np.random.randint(-10000, 10001, size=1000)

# Создаем объект Series
numbers_series = pd.Series(random_num)

min_num = numbers_series.min()
print(f'Минимальное значение в Series: {min_num}')

count_num = numbers_series.value_counts()
print(f'Количество повторяющихся значений: {count_num}')

max_num = numbers_series.max()
print(f'Максимальное значение в Series: {max_num}')

sum_num = numbers_series.sum()
print(f'Сумма всех значений в Series: {sum_num}')

cv_num = numbers_series.std()
print(f'Среднеквадратичное отклонение в Series: {cv_num}')

new_series = numbers_series.round(-2)
#Пострим линейный график
plt.figure(figsize=(15,5))
plt.plot(numbers_series, linestyle = '-', color = 'b')
plt.title("Линейный график")
plt.xlabel('Ось x: ')
plt.ylabel('Ось y: ')
plt.grid()
plt.show()
#Построим гистограмму(прямоугольную)
plt.figure(figsize=(15,5))
plt.hist(new_series, bins = 200, edgecolor = 'black', alpha = 0.6)
plt.xlabel('Ось x: ')
plt.ylabel('Ось y: ')
plt.title('Прямоугольная гистограмма')
plt.grid()
plt.show()

# Создание DataFrame из Series
data_frame = pd.DataFrame({'Digit': numbers_series})

data_frame['Отсортированные по возрастанию'] = np.sort(numbers_series)
data_frame['Отсортированные по убыванию'] = np.sort(numbers_series)[::-1]



plt.figure(figsize=(15,5))
plt.plot(data_frame['Отсортированные по возрастанию'].values, label = 'По возрастанию', color = 'green')
plt.plot(data_frame['Отсортированные по убыванию'].values, label = 'По убыванию', color = 'red')
plt.xlabel('Ось x: ')
plt.ylabel('Ось y: ')
plt.title("Сравнение отсортированных значений")
plt.legend()
plt.show()