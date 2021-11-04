#輸入保齡球的配置參數
list1=[int(i) for i in input().split()]
N=list1[0]
K=list1[1]
#輸入參數並建立二維陣列
list2=[]
for i in range(K):
    list2.append([int(e) for e in input().split()])
#打保齡球
list3=['I']*N
for i in range(K):
    for j in range(list2[i][0]-1, list2[i][1]):
        list3[j] = '.'
#剩下多少個pins，印出來
print(''.join(list3))