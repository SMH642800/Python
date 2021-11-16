Nr, Nc = [int(i) for i in input().split()]
a = [[int(e) for e in input().split()] for i in range(Nr)]
for i in range(Nc):
    for j in range(Nr-1):
        print(a[j][i], end=' ')
    print(a[Nr-1][i])
