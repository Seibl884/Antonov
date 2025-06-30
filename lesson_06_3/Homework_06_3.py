lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

for item in lst1:
    if isinstance(item, str):
        lst2.append(item)

print(f"Исходный список (lst1): {lst1}")
print(f"Новый список со строками (lst2): {lst2}")