N = int(input())
A = (input()).split(' ')
Turn = 0
r = []
for i in A:
    number = A[N-1-Turn]
    if i == A[0]:
        r += str(number)
        Turn += 1
    else:
        r += ' ' + str(number)
        Turn += 1

print(r)

## if we have 4 intergers, we want 0-3, 1-2, 2-1, 3-0
## example 3 9 2 0 -> 0 2 9 3