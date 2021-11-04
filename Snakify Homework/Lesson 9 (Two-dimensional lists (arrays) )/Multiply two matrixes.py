#輸入m, n, r的值，建立 (m*n) 和 (n*r) 的A,B二維陣列
m, n, r = [int(i) for i in input().split()]
A = [[int(e) for e in input().split()]for i in range(m)]
B = [[int(e) for e in input().split()]for i in range(n)]
#A*B 陣列相乘輸入到C陣列
C = [[0]*r for _ in range(m)]
for i in range(m):
    for j in range(r):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]
#印出陣列
for i in range(m):
    for j in range(r):
        print(C[i][j], end=' ')
    print()