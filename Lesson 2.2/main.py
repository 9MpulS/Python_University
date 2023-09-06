# структуда програми
from microzaim import microzaim

A = int(input('Enter the value of the monthly stipend: '))
B = int(input('Enter the value of your monthly expenses: '))
while B < A:
    print('Monthly expenses should be more than the stipend!')
    B = int(input('Enter the value of your monthly expenses: '))

ans = microzaim(A, B)   # Обчислюємо суму грошей, яку необхідно попросити в батьків
print('The amount of money you need to ask your parents for: ', ans)