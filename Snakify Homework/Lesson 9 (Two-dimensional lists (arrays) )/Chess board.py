Nr, Nc = map(int, input().split())
A = [['.']*Nc for _ in range(Nr)]

for i in range(Nr):
    for j in range(Nc):
        if i%2 == 0:
            if j%2 == 1:
                A[i][j] = '*'
        elif i%2 == 1:
            if j%2 == 0:
                A[i][j] = '*'

for i in range(Nr):
    print(' '.join(A[i]))