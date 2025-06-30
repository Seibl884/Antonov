numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even_sum = 0

for number in numbers:
    if number % 2 == 0:  # Проверяем, является ли число четным
        even_sum += number

print(f"Список чисел: {numbers}")
print(f"Сумма всех четных чисел: {even_sum}")