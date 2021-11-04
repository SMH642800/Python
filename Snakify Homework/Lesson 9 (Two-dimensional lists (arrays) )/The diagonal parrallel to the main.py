#輸入數字n，形成一個預設元素為0的n*n二維陣列
n = int(input())
A=[['0']*n for _ in range(n)]
#元素的內容值 == row值-column值的相差值
for i in range(n):
    for j in range(n):
            A[i][j] = str(abs(i-j))
#印出二維陣列
for i in range(n):
    print(' '.join(A[i]))
