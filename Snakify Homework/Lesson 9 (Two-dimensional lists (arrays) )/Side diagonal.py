#輸入一個值n，形成一個元素預設值為0的n*n二維陣列
n = int(input())
A=[['0']*n for _ in range(n)]
#從右上到左下斜角線元素值為1，右下區域為2
for i in range(n):
    for j in range(n):
        if i+j == n-1:
            A[i][j] = '1'
        if j >= n-i:
            A[i][j] = '2'
#印出陣列
for i in range(n):
    print(' '.join(A[i]))