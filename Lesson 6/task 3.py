set_A = set(input("Введіть множину А через пробіл:").split())
element_x = input("Введіть елемент Х:")

def form_set_B(set_A, element_x):
    if element_x in set_A:
        set_A.remove(element_x)
    else:
        set_A.add(element_x)

form_set_B(set_A, element_x)

print("Множина B:", set_A)
