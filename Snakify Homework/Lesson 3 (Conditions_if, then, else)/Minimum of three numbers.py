a=int(input())
b=int(input())
c=int(input())

if a>b:
    a,b=b,a
    if a>c:
        print(c)
    else:
        print(a)
else:
    if a<c:
        print(a)
    else:
        print(c)