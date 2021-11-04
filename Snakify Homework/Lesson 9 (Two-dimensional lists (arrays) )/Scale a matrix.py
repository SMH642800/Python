row_num, column_num = [int(i) for i in input().split()]
list1=[[int(e) for e in input().split()] for i in range(row_num)]
scale = int(input())

for i in range(row_num):
    for j in range(column_num):
        print(list1[i][j]*scale, end=' ')
    print()