print('___All values must be greater than 0!___')
a = int(input("Enter а: "))
while a < 1:
    a = int(input("Enter а again: "))

b = int(input("Enter b: "))
while b < 1:
    b = int(input("Enter b again: "))

if a < b:
    ans = a/b+5
elif a == b:
    ans = -1
else:
    ans = (a*b-5)/a
print("Your answer is: ", ans)