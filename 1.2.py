# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60
time_new_format = "{}:{}:{}".format(hours, minutes, seconds)
print(time_new_format)