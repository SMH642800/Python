list_A=[int(i) for i in input().split()]
unique_list=[]
list_B=[]
for i in list_A:
    if i not in unique_list:
        unique_list.append(i)
    else:
        list_B.append(i)
list_C=set(unique_list).difference(list_B)
for e in list_C:
    print(e, end=' ')
