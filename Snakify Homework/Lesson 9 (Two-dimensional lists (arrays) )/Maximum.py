row_num, column_num = [int(i) for i in input().split()]
list1 = [[int(e) for e in input().split()] for i in range(row_num)]

Max_num = list1[0][0]
Mr = Mc = 0

for i in range(row_num):
    for j in range(column_num):
        if list1[i][j]>Max_num:
            Max_num=list1[i][j]
            Mr, Mc=i, j

print(Mr,Mc)