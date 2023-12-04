import re

def a(filename):
    with open(filename, 'w') as file:
        lines = [
            "This sentence is of varying length.",
            "Another sentence with a few words!",
            "There will be a string without doubling letters.",
            "But this one has a doubling of letters: slovoo."
        ]
        file.write('\n'.join(lines))

def find_double_letters_words(input_text):
    words = re.findall(r'\b(\w*(\w)\2\w*)\b', input_text)
    return [word[0] for word in words]

def b(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        input_text = input_file.read()
        double_letter_words = find_double_letters_words(input_text)

        if double_letter_words:
            output_file.write('\n'.join(double_letter_words))
        else:
            output_file.write("Немає слів із подвоєнням букв.")

def v(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)


tf7_1_filename = "TF7_1.txt"
tf7_2_filename = "TF7_2.txt"

# а) Створити текстовий файл TF7_1
a(tf7_1_filename)

# б) Обробити TF7_1 та створити TF7_2
b(tf7_1_filename, tf7_2_filename)

# в) Вивести вміст файла TF7_2
v(tf7_2_filename)
