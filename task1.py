text = input("Введіть текст: ")
letter = input("Введіть літеру: ")

text = text.lower()
letter = letter.lower()

words = text.split()

count = 0

for word in words:
	if word.startswith(letter):
		count += 1

print(f"Кількість слів, що починаються з літери '{letter}' без врахування регістру: {count}")