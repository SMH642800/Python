n = int(input())
result = []
for i in range(n):
    a, b = [int(e) for e in input().split()]
    result.append(a+b)
for i in range(n):
    print(result[i], end='\n')