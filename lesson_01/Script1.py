# task 01 == Виправте синтаксичні помилки﻿

print("Hello", end = " ")

print("world!")

# task 02 == Виправте синтаксичні помилки

hello = "Hello"

world = "world"

if True:

    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print

for letter in "Hello world!":

    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була

# завжди в чотири рази більша, ніж яблук

apples = 4

banana = apples * 4

print (apples)

print (banana)

# task 05 == виправте назви змінних

storona_1 = 1

storona_2 = 2

storona_3 = 3

storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05

# та виведіть його для користувача

perimeter = storona_1 + storona_2 + storona_3 + storona_4

print("Периметр фігури =", perimeter)

"""

    # Задачі 07 -10:

    # Переведіть задачі з книги "Математика, 2 клас"

    # на мову пітон і виведіть відповідь, так, щоб було

    # зрозуміло дитині, що навчається в другому класі

"""

# task 07

"""

У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.

Скільки всього дерев посадили в саду?

"""

apple_trees = 4

pear_trees = apple_trees + 5

plum_trees = apple_trees - 2

total_trees = apple_trees + pear_trees + plum_trees

print("Всього дерев у саду:", total_trees)

# task 08

"""

До обіда температура повітря була на 5 градусів вище нуля.

Після обіду температура опустилася на 10 градусів.

Надвечір потепліло на 4 градуси. Яка температура надвечір?

"""

temperature_morning = 5

temperature_after_lunch = temperature_morning - 10

temperature_evening = temperature_after_lunch + 4

print("Температура надвечір:", temperature_evening, "градусів")

# task 09

"""

Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.

1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.

Скількі сьогодні дітей у театральному гуртку?

"""

boys = 24

girls = boys // 2

boys_today = boys - 1

girls_today = girls - 2

total_today = boys_today + girls_today

print("Сьогодні у гуртку дітей:", total_today)

# task 10

"""

Перша книжка коштує 8 грн., друга - на 2 грн. дороже,

а третя - як половина вартості першої та другої разом.

Скільки будуть коштувати усі книги, якщо купити по одному примірнику?

"""

book1 = 8

book2 = book1 + 2

book3 = (book1 + book2) / 2

total_price = book1 + book2 + book3

print("Вартість усіх книг:", total_price, "грн.")