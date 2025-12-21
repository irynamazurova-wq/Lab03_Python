text = input("Введіть текст українською мовою: ").strip()

#очищення від зайвих пробілів
words = text.split()
half = len(words) // 2

#перша половина - перша літера великою
first_half = [w.capitalize() for w in words[:half]]

#друга половина: видаляємо всі розділові знаки всі літери маленькі + *
second_half = []
for w in words[half:]:
    clean_word = w.strip(",.!?;:-()")
    second_half.append(clean_word.lower() + "*")

#формуємо новий рядок з символом "|" посередині
result = " ".join(first_half) + " | " + " ".join(second_half)
print("Результат:\n", result)
