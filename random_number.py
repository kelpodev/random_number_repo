import random

print("Генератор случайных чисел")
min_value = int(input("Введите минимальное число: "))
max_value = int(input("Введите максимальное число: "))
if min_value <= max_value:
    result = random.randint(min_value, max_value)
    print(f"Случайное число: {result}")
else:
    print("Ошибка: минимальное число больше максимального")
