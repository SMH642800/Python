list1=[int(e) for e in input().split()]
list1.sort()
element=list1[0]
count=1
for e in range(1,len(list1)):
    if list1[e]==element:
        element = list1[e]
    else:
        count+=1
        element=list1[e]
print(count)