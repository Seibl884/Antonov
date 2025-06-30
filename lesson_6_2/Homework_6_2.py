while True:
    word = input("Введите слово, содержащее букву 'h': ")
    if 'h' in word.lower():
        print(f"Отлично! Слово '{word}' содержит букву 'h'.")
        break
    else:
        print(f"Слово '{word}' не содержит букву 'h'. Попробуйте еще раз.")