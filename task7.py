text = input("Введіть текст англійською мовою: ").strip()

#видаляємо основні розділові знаки
for ch in ",.!?;:-()":
    text = text.replace(ch, "")

#розділяємо текст на слова
words = text.split()

#слова, що починаються з великої літери
capital_words = [w for w in words if w[0].isupper()]

print("Імена та власні назви:\n", capital_words)
