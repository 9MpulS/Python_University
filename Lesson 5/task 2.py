N = int(input("Введіть розмірність матриці: "))

print(f"Матриця розміром {N}x{N} відповідно до зразка:")
a = []


for i in range(N):
    row = []
    for j in range(N):
        if i + j >= N-1:
            row.append(2*N-j-i-1)
        else:
            row.append(0)
    a.append(row)

for r in a:
    print(*r)
