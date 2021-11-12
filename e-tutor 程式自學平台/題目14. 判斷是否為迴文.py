n = input()
if len(n)%2 == 0:
    count = 0
    for i in range(len(n)//2):
        if n[i] != n[len(n)-1-i]:
            count+=1
else:
    count = 0
    for i in range(len(n) // 2):
        if n[i] != n[len(n)-1-i]:
            count += 1
if count == 0:
    print('YES')
else:
    print('NO')
