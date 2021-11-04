#輸入一個值row和column的數量，形成一個Nr*Nc的二維陣列
Nr, Nc = [int(i) for i in input().split()]
A = [[int(j) for j in input().split()] for i in range(Nr)]
'''
A = []
for i in range(Nr):
    A.append([int(e) for e in input().split()])
'''
#輸入要對調的column
c1, c2 = [int(i) for i in input().split()]
for i in range(Nr):
        A[i][c1], A[i][c2] = A[i][c2], A[i][c1]
#印出陣列
for i in range(Nr):
    for j in range(Nc):
        print(A[i][j], end=' ')
    print()
'''
print('\n'.join([' '.join([str(i) for i in row]) for row in a]))
'''