import string  #для списку розділових знаків

text = input("Введіть текст: ")
target_word = input("Введіть слово для пошуку: ")

if not text or not target_word:
    print("Помилка вводу.")
else:
    for char in string.punctuation:
        text = text.replace(char, " ")

    words = text.split()

    #рахуємо кількість (ігноруємо регістр: Слово == слово)
    count = 0
    for w in words:
        if w.lower() == target_word.lower():
            count += 1

    print(f"Задане слово '{target_word}' зустрічається разів: {count}")