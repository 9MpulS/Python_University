import json

def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

def write_json_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def display_json_content(filename):
    data = read_json_file(filename)
    print("Вміст JSON файлу:")
    print(json.dumps(data, indent=2))

def add_student(data, last_name, first_name, middle_name, birth_year, birth_month, birth_day, gender):
    new_student = {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'birth_date': {
            'year': birth_year,
            'month': birth_month,
            'day': birth_day
        },
        'gender': gender
    }
    data.append(new_student)
    return data

def remove_student(data, last_name, first_name):
    data = [student for student in data if not (student['last_name'] == last_name and student['first_name'] == first_name)]
    return data

def search_students_by_birth_month(data, search_month):
    matching_students = [student for student in data if student['birth_date']['month'] == search_month]
    return matching_students

def main():
    json_filename = "students.json"

    while True:
        print("\n1. Вивести вміст JSON файлу")
        print("2. Додати нового учня")
        print("3. Видалити учня")
        print("4. Пошук учнів за місяцем народження")
        print("5. Вийти")

        choice = input("Виберіть опцію (1-5): ")

        if choice == '1':
            display_json_content(json_filename)
        elif choice == '2':
            last_name = input("Прізвище: ")
            first_name = input("Ім'я: ")
            middle_name = input("По батькові: ")
            birth_year = int(input("Рік народження: "))
            birth_month = int(input("Місяць народження: "))
            birth_day = int(input("День народження: "))
            gender = input("Стать: ")
            students_data = add_student(read_json_file(json_filename), last_name, first_name, middle_name,
                                        birth_year, birth_month, birth_day, gender)
            write_json_file(students_data, json_filename)
        elif choice == '3':
            last_name = input("Прізвище учня, якого потрібно видалити: ")
            first_name = input("Ім'я учня, якого потрібно видалити: ")
            students_data = remove_student(read_json_file(json_filename), last_name, first_name)
            write_json_file(students_data, json_filename)
        elif choice == '4':
            search_month = int(input("Введіть місяць для пошуку: "))
            matching_students = search_students_by_birth_month(read_json_file(json_filename), search_month)
            if matching_students:
                print("\nУчні з народженням у вказаному місяці:")
                for student in matching_students:
                    print(f"{student['first_name']} {student['last_name']}")
            else:
                print("Немає учнів з народженням у вказаному місяці.")
        elif choice == '5':
            break
        else:
            print("Невірний вибір. Введіть число від 1 до 5.")

if __name__ == "__main__":
    main()
