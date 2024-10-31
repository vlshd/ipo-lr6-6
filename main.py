import random
from itertools import combinations

random_list = [[random.randint(-10, 10) for _ in range(4)] for _ in range(20)] # создание случайного списка
list = [item for sublist in random_list for item in sublist] # извлечение всех значений в один плоский список
unikal = list(combinations(list, 2)) # нахождение уникальных комбинаций пар
user_value = int(input("Введите целое число: ")) # запрос числа
count_less_than_user_value = sum(1 for pair in unikal if sum(pair) < user_value) # количества пар, чья сумма меньше заданного значения
print("Случайный список:", list) # вывод
print("Уникальные комбинации пар:", unikal) # вывод
print(f"Количество пар, чья сумма меньше {user_value}: {count_less_than_user_value}") # вывод
