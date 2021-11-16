num = [int(e) for e in input().split()]
min_num = num[0]
count = 1
for i in range(0,2):
    if min_num>num[i+1]:
        min_num = num[i+1]
    if min_num == num[i+1]:
        count += 1
if count == 1:
    print(min_num)
else:
    print(' '.join(str(min_num)*count))