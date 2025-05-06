import numpy as np


a = np.arange(1, 11)
print(a)



a = np.array([5, 10, 15, 20])

print("Сумма:", np.sum(a))      # 50
print("Среднее:", np.mean(a))   # 12.5


a = np.array([3, 6, 9, 12])

normalized = (a - a.min()) / (a.max() - a.min())
print(normalized)

a = np.array([10, 25, 5, 40])

filtered = a[a > 15]
print(filtered)  # → array([25, 40])

a = np.arange(1, 10).reshape((3, 3))
print("Матрица:")
print(a)

print("Сумма по столбцам:", np.sum(a, axis=0))
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])


print("Максимум по строкам:", np.max(a, axis=1))  # [3 6 9]
print("Максимум по столбцам:", np.max(a, axis=0))  # [7 8 9]

# Стандартное отклонение показывает, насколько сильно значения "разбегаются" от среднего.

a = np.array([10, 12, 14, 16, 18])

print("Стандартное отклонение:", np.std(a))  # → 2.828...
a = np.array([1, 5, 3, 7, 2])
a[a < 4] = 0  # Замена всех значений меньше 4 на 0.
print(a)  # → [0 5 0 7 0]

a = np.array([1, 3, 5])
b = np.array([2,4,6])
sum_ab = a + b
print("Сумма массивов: ", sum_ab)
print("Произведение массива а: ", (a * 3))

sales = np.array([[10, 15, 20, 25],
                  [5, 10, 15, 20],
                  [8, 12, 18, 22],
                  [7, 9, 14, 17],
                  [6, 8, 10, 12]])

sales = np.array([[10, 15, 20, 25],
                  [5, 10, 15, 20],
                  [8, 12, 18, 22],
                  [7, 9, 14, 17],
                  [6, 8, 10, 12]])


sum_cvartal = np.sum(sales, axis = 0) # сумма по регионам
mean_cvartal = np.mean(sales, axis=0) # средняя сумма по всем регионам за кварталы
std_cvartal = np.std(sales, axis=1) # стандартное отклонение
median_cvartal = np.median(sales) # медиана

for i, val in enumerate(sum_cvartal, 1):
    print(f"Сумма продаж по всем регионам за {i} квартал: {val}")
print("\nСумма продаж по всем регионам за все кварталы: ", np.sum(sales))
print()

for i, val in enumerate(mean_cvartal, 1):
    print(f"Средняя сумма продаж за {i} квартал: {val}")

print()

for i, val in enumerate(std_cvartal, 1):
    print(f"Стандартное отклонение по продажам {i} региона: {val}")

print("\nМедиану для всех данных о продажах: ", median_cvartal)


grades = np.array([
    [5, 4, 5, 5],
    [3, 4, 4, 3],
    [5, 5, 5, 5],
    [4, 4, 4, 4],
    [5, 5, 4, 5],
    [2, 3, 2, 3]
])

average_grades = np.mean(grades, axis=1)
print("Средний балл каждого студента:", average_grades)

count_high_achievers = np.sum(average_grades > 4.0)
print("Количество студентов со средним баллом выше 4.0:", count_high_achievers)

min_avg = np.min(average_grades)
max_avg = np.max(average_grades)
print("Минимальный средний балл:", min_avg)
print("Максимальный средний балл:", max_avg)

count_honors = np.sum(np.all(grades == 5, axis=1))
print("Количество отличников:", count_honors)

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Среднее по столбцам
mean_data = np.mean(data, axis=0)

# Медиана по строкам
median_data = np.median(data, axis=1)

print("Среднее по столбцам: ", mean_data)
print("Медиана по строкам: ", median_data)
