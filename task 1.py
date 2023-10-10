N = int(input("Введіть кількість елементів у масиві: "))

arr = []


print("Заповніть масив числами:")
for i in range(N):
    num = int(input())
    arr.append(num)

print("Додатні числа в масиві в зворотньому порядку:")
for x in reversed(arr):
    if x > 0:
        print(x)