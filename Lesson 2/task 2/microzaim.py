# код в модулі
def microzaim(stipend, fst_expenses):   # ф-я для розрахунку суми грошей, яку необхідно попросити в батьків
    lst_expenses = fst_expenses
    total = 0
    for i in range(10):
        total += lst_expenses
        lst_expenses *= 1.05
    return total - (stipend*10)  # витрати за рік мінус стипендія за рік
