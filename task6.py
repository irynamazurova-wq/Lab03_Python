text = input("Введіть текст англійською: ").lower()

#список голосних літер англ мови
vowels = "aeiou"

#підрахунок кількості голосних
count = sum(1 for c in text if c in vowels)

print("Кількість голосних літер:", count)
