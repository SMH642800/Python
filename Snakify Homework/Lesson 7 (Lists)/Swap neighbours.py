list1=[int(i) for i in input().split()]
if len(list1)%2==0:
    for i in range(0, len(list1), 2):
        list1[i], list1[i + 1] = list1[i + 1], list1[i]
else:
    for i in range(0, len(list1)-1, 2):
        list1[i], list1[i + 1] = list1[i + 1], list1[i]
for j in list1:
    print(j, end=' ')