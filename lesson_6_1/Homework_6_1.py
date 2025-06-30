# Получаем строку от пользователя
input_string = input("Пожалуйста, введите строку: ")

# Используем множество (set) для хранения уникальных символов.
# Множества автоматически удаляют дубликаты.
unique_characters = set(input_string)

# Считаем количество уникальных символов
count_unique = len(unique_characters)

# Проверяем условие и выводим результат
if count_unique > 10:
    print(True)
else:
    print(False)