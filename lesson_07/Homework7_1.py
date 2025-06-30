# task 1
""" Задача - напечатать таблицу умножения на заданное число, но
только до максимального значения произведения - 25.
Код почти готов, нужно найти ошибки и исправить/дополнить.
"""
def multiplication_table(number):
    multiplier = 1
    while True:
        result = number * multiplier
        if result > 25:
            break
        print(f"{number}x{multiplier}={result}")
        multiplier += 1

multiplication_table(3)
# Должно вывести:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
# 3x6=18
# 3x7=21
# 3x8=24

# task 2
""" Написать функцию, которая вычисляет сумму двух чисел.
"""
def sum_two_numbers(a, b):
    """Возвращает сумму двух чисел."""
    return a + b

# task 3
""" Написать функцию, которая вычисляет среднее арифметическое списка чисел.
"""
def average(numbers):
    """Возвращает среднее арифметическое списка чисел."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# task 4
""" Написать функцию, которая принимает строку и возвращает её в обратном порядке.
"""
def reverse_string(s):
    """Возвращает строку в обратном порядке."""
    return s[::-1]

# task 5
""" Написать функцию, которая принимает список слов и возвращает самое длинное слово в списке.
"""
def longest_word(words):
    """Возвращает самое длинное слово из списка."""
    if not words:
        return ""
    return max(words, key=len)

# task 6
""" Написать функцию, которая принимает две строки и возвращает индекс первого вхождения второй строки
в первую строку, если вторая строка является подстрокой первой строки, и -1, если не является.
"""
def find_substring(str1, str2):
    """Возвращает индекс первого вхождения str2 в str1, либо -1 если не найдено."""
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # вернет 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # вернет -1
# --- Task 10: 4 функции из предыдущих домашних работ ---

def calculate_sum(number_one, number_two):
    """
    Возвращает сумму двух предоставленных чисел.

    Args:
        number_one (int/float): Первое число для сложения.
        number_two (int/float): Второе число для сложения.

    Returns:
        int/float: Результат сложения number_one и number_two.
    """
    return number_one + number_two

def calculate_list_average(list_of_numbers):
    """
    Вычисляет среднее арифметическое чисел в заданном списке.

    Args:
        list_of_numbers (list): Список чисел (целых или с плавающей точкой).

    Returns:
        float: Среднее арифметическое значение. Возвращает 0.0, если список пуст,
               чтобы избежать ошибки деления на ноль.
    """
    if not list_of_numbers:
        return 0.0
    total_sum = sum(list_of_numbers)
    return total_sum / len(list_of_numbers)

def get_reversed_string(original_string):
    """
    Возвращает заданную строку в обратном порядке.

    Args:
        original_string (str): Исходная строка для разворота.

    Returns:
        str: Строка, символы которой расположены в обратном порядке.
    """
    return original_string[::-1]

def get_longest_word_from_list(words_collection):
    """
    Находит и возвращает самое длинное слово из списка слов.

    Args:
        words_collection (list): Список строк (слов).

    Returns:
        str: Самое длинное слово. Если список пуст, возвращает пустую строку.
    """
    if not words_collection:
        return ""
    
    current_longest_word = ""
    for word_item in words_collection:
        if len(word_item) > len(current_longest_word):
            current_longest_word = word_item
    return current_longest_word

# --- Примеры использования функций из Task 10 ---
print("\n--- Примеры использования функций из Task 10 ---")
print(f"Сумма 7 и 8: {calculate_sum(7, 8)}")

my_grades = [85, 90, 78, 92]
print(f"Средний балл: {calculate_list_average(my_grades)}")

phrase = "Hello Python"
print(f"Обратная строка '{phrase}': {get_reversed_string(phrase)}")

city_names = ["Kyiv", "London", "Paris", "Washington"]
print(f"Самый длинный город: {get_longest_word_from_list(city_names)}")