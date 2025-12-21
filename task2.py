text = input("Введіть текст: ")

if not text:
    print("Помилка: введіть дані.")
else:
    replaced_text = text.replace('а', 'А')
    replacements = text.count('а')
    letters = sum(c.isalpha() for c in text)
    symbols = len(text)

    print("Змінений текст:", replaced_text)
    print("Кількість замін:", replacements)
    print("Кількість символів:", symbols)
    print("Кількість літер:", letters)

