text = input("Введіть текст англійською мовою: ").strip()

start_letter = input("Введіть початкову літеру (N): ").upper()
end_letter = input("Введіть кінцеву літеру (P): ").upper()

#перевіряємо, чи введені символи англійські літери
if not (start_letter.isalpha() and end_letter.isalpha()):
    print("Помилка: введені символи не є літерами.")
else:
    words = text.replace(",", "").replace(".", "").split()
    #вибираємо слова, що починаються на start_letter і закінчуються на end_letter
    result = [w for w in words if w.upper().startswith(start_letter) or w.upper().endswith(end_letter)]
    print("Слова, що починаються на N або закінчуються на P:\n", result)
