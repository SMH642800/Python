list1=[int(i) for i in input().split()]
max_num=max(list1)
min_num=min(list1)
index_max=list1.index(max_num)
index_min=list1.index(min_num)
list1[index_max]=min_num
list1[index_min]=max_num
for i in list1:
    print(i, end=' ')