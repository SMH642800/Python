n = int(input())
a = set()
lines = [input().split() for i in range(n)]
for line in lines:
    for word in line:
        if word not in a:
            a.add(word)
print(len(a))