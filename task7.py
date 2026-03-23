import string

text = input("Введіть текст англійською мовою: ").strip()
for ch in string.punctuation:
    text = text.replace(ch, "")
words = text.split()
capital_words = [w for w in words if w[0].isupper()]
vowels = "aeiou"
count = sum(1 for c in text.lower() if c in vowels)
print("Імена та власні назви:\n", capital_words)
print("Кількість голосних літер:", count)
