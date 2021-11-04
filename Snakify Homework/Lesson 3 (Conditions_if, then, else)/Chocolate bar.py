n=int(input())
m=int(input())
k=int(input())

if k>=(n*m):
    print('NO')
elif k<=0:
    print('NO')
else:
    if (k%1)==0:
        if (k/n)<=m and (k%n)==0:
            print('YES')
        elif(k/m)<=n and (k%m)==0:
            print('YES')
        else:
            print('NO')
    else:
        ('NO')