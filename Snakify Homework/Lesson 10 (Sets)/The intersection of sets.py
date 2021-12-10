a = set(input().split())
b = set(input().split())
c = sorted(a&b)
for i in c:
    print(i, end=' ')