def find_first_five_min(input_list):
    # Використовуємо функцію sorted() для сортування списку за зростанням
    sorted_list = sorted(input_list)

    first_five_min = sorted_list[:5]

    return first_five_min


user_input = input("Введіть елементи списку через пробіл: ")
user_list = user_input.split()  # Розділяємо введений рядок на окремі елементи списку

int_user_list = []

# Перетворюємо елементи списку на цілі числа за допомогою циклу
for item in user_list:
    int_item = int(item)
    int_user_list.append(int_item)

first_five_min = find_first_five_min(int_user_list)

print("Перші п'ять мінімальних елементів:", first_five_min)