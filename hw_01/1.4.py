# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

value = int(input("Введите целое положительное число: "))
max_number = 0
while value > 0:
    number = value % 10
    if number > max_number:
        max_number = number
    value //= 10
print("Самая большая цифра: ", max_number)
