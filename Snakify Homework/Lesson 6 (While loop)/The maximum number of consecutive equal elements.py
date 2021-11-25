n = int(input())
count = 0
max = 0
temp = n
while n != 0:
    if temp == n:
        count += 1
        if max < count:
            max = count
    else:
        if max < count:
            max = count
        temp = n
        count = 1
    n = int(input())
print(max)