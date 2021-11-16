#輸入一個值n，形成一個元素預設值為0的nn二維陣列
n = int(input())
A=[['0']n for _ in range(n)]
#從右上到左下斜角線元素值為0
#該對角線以上的元素，與對角線的y軸垂直距離為i時，該數值為-i
#該對角線以下的元素，與對角線的y軸垂直距離為i時，該數值為i
a = n-1
for i in range(n)
    for j in range(n)
        A[i][j] = str(j-a)
    a -= 1
#印出陣列
for i in range(n)
    print(' '.join(A[i]))