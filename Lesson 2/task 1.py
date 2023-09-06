import math
def calc_Z(alpha):  # ф-я для розрахунку z=cos^2α+cos^4α
    z = math.cos(alpha)**2 + math.cos(alpha)**4
    return z
def microzaim(stipend, fst_expenses):   # ф-я для розрахунку суми грошей, яку необхідно попросити в батьків
    lst_expenses = fst_expenses
    total = 0
    for i in range(10):
        total += lst_expenses
        lst_expenses *= 1.05
    return total - (stipend*10)  # витрати за рік мінус стипендія за рік

print('Expression: z=cos^2α+cos^4α')
alpha = float(input("Enter the value of alpha: "))  # обчислюємо z та виводимо результат
z = calc_Z(alpha)
print('Answer: ', z)
print('_______________________________________________________')

A = int(input('Enter the value of the monthly stipend: '))
B = int(input('Enter the value of your monthly expenses: '))
while B < A:
    print('Monthly expenses should be more than the stipend!')
    B = int(input('Enter the value of your monthly expenses: '))

ans = microzaim(A, B)   # Обчислюємо суму грошей, яку необхідно попросити в батьків
print('The amount of money you need to ask your parents for: ', ans)