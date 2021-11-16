n = int(input())
if n < 0:
    n += 256
#使用bin函數來取得二進位: 0bxxxxx...
m=bin(n)
#list(a) 取得二進位數字作為字串
a=m[2:]
#把string填滿8個位子，填充0進去
print(a.zfill(8))