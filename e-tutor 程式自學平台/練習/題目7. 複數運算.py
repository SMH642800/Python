n=int(input())
result = [[0]*2 for _ in range(n)]
for i in range(n):
    w,a1,a2,b1,b2=map(str,input().split())
    a1=int(a1)
    a2=int(a2)
    b1=int(b1)
    b2=int(b2)
    if w=='+':
        result[i][0] = a1+b1
        result[i][1] = a2+b2
    elif w=='-':
        result[i][0] = a1 - b1
        result[i][1] = a2 - b2
    elif w=='*':
        result[i][0] = a1*b1-a2*b2
        result[i][1] = a2*b1+a1*b2
    else:
        result[i][0] = (a1*b1+a2*b2)/(b1*b1+b2*b2)
        result[i][1] = (a2*b1-a1*b2)/(b1*b1+b2*b2)
for i in range(n):
    for j in range(1):
        print(result[i][j], end=' ')
        print(result[i][1])
