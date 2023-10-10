def remove_duplicates(input_list):
    unique_list = []  # Створюємо порожній список для унікальних значень

    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)  # Додаємо елемент до унікального списку, якщо його там немає

    return unique_list

# Зчитуємо список з клавіатури
user_input = input("Введіть елементи списку через пробіл: ")
user_list = user_input.split()  # Розділяємо введений рядок на окремі елементи списку

# Викликаємо функцію для видалення повторень
unique_list = remove_duplicates(user_list)

# Виводимо унікальний список на екран
print("Список без повторень:", unique_list)
