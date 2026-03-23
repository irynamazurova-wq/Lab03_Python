text = input("Введіть текст: ")
letter = input("Введіть літеру: ")

if not text or not letter or len(letter) != 1:
    print("Помилка: некоректні вхідні дані.")
else:
    text = text.lower()
    letter = letter.lower()
    words = text.split()
    count = sum(1 for word in words if word.startswith(letter))
    print(f"Кількість слів, що починаються з літери '{letter}': {count}")
