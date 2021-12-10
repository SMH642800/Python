n = int(input())
s = []
res = []
for i in range(n):
    s.append(input())
for i in range(n):
    sum = 0
    for j in s[i]:
        sum += int(ord(j))
    res.append(sum)
for i in res:
    print(i)
