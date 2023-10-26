import datetime

students = {}

# Функція для видалення інформації про учня
def del_student(students, student_id):
    del students[student_id]

# Функція для додавання інформації про учня
def add_student(students, student_id, прізвище, ім_я, по_батькові, рік, місяць, число):
    students[student_id] = {
        "прізвище": прізвище,
        "ім_я": ім_я,
        "по батькові": по_батькові,
        "дата_народження": (рік, місяць, число)
    }

# Початкова інформація про учнів за допомогою функції
add_student(students, 1, "Іванов", "Іван", "Петрович", 2006, 5, 15)
add_student(students, 2, "Петров", "Петро", "Іванович", 2007, 10, 26)
# Додайте іншу інформацію про інших учнів

today = datetime.date.today()

while True:
    print("Для додавання інформації введіть 'add'\nДля видалення інформації введіть 'del'\nДля пошуку іменинників введіть 'birth'\nДля вимкнення програми введіть 'end'")
    comnd = input("Введіть команду: ")
    if comnd == "add":
        student_id = len(students) + 1
        print("Заповніть данні про учня")
        sname, name, fname = map(str, input("Прізвище, ім_я, по батькові (через пробіл): ").split())
        year, month, day = map(int, input("Рік, місяць, день народження (через пробіл): ").split())
        add_student(students, student_id, sname, name, fname, year, month, day)
        print(f"Учня {sname} {name} {fname} було додано до словника")

    if comnd == "del":
        print("Виберіть учня, інформацію про якого хочете видалити: ")
        for student_id, student_info in students.items():
            print(student_id, student_info)
        key = int(input("Введіть номер учня: "))
        if key in students:
            del_student(students, key)
            print(f"Інформацію про учня з номером {key} було видалено")
        else:
            print("Учня з таким номером не знайдено")

    if comnd == "birth":
        found = False
        for student_id, student_info in students.items():
            birthdate = datetime.date(student_info["дата_народження"][0], student_info["дата_народження"][1], student_info["дата_народження"][2])
            if birthdate.month == today.month and birthdate.day == today.day:
                print(f'Сьогодні день народження у {student_info["ім_я"]} {student_info["прізвище"]}')
                found = True
        if not found:
            print("Сьогодні нічийого дня народження")

    if comnd == "end":
        break
