#輸入參數並建立二維陣列
list1=[]
for i in range(8):
    list1.append([int(e) for e in input().split()])
#判斷是否能夠互相走到對方的位子
count_all=0
for i in range(8):
    for j in range(i+1,8):
        for k in range(2):
            if list1[i][k] == list1[j][k]:
                count_all+=1
        if abs(list1[i][0]-list1[j][0]) == abs(list1[i][1]-list1[j][1]):
            count_all+=1
#判斷count_all是否大於1
if count_all > 0:
    print('YES')
else:
    print('NO')