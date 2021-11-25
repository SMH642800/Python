num = int(input())
list1 = []
while num != 0:
    list1.append(num)
    num = int(input())
list1.sort()
print(list1[-2])