text = input("Введіть речення: ")
words = text.split()
count = 0
for word in words:
    if word.endswith("р"):
        count += 1
print("Кількість слів, які закінчуються на 'р': ", count)
