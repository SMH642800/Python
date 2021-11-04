n = int(input())
A = [['.']*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == (n//2):
            A[i][j] = '*'
        elif j == (n//2):
            A[i][j] = '*'
        elif i == j:
            A[i][j] = '*'
        elif abs(i+j) == n-1:
            A[i][j] = '*'

for i in range(n):
    print(' '.join(A[i]))