n = int(input())
number = n - 1
while number > 1:
    n *= number
    print(n)
    number -= 1
print(n)