temp = int(input('Enter the height of the pyramid, which does not exceed 9: '))
while temp > 9 or temp < 1:
    temp = int(input('Enter the height of the pyramid again, which does not exceed 9: '))
for i in range(temp):
    n = temp
    for k in range(temp):
        if k >= i:
            print(n, end=' ')
            n -= 1
    print('')