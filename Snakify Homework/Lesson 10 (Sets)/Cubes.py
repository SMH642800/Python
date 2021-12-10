n, m = input().split()
a = set()
b = set()
for i in range(int(n)):
    a.add(int(input()))
for i in range(int(m)):
    b.add(int(input()))
print(len(a&b))
for i in a&b:
    print(i)
print(len(a-b))
for i in sorted(a-b):
    print(i)
print(len(b-a))
for i in b-a:
    print(i)