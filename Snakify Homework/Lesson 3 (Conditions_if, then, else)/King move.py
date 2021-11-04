x=int(input())
y=int(input())
a=int(input())
b=int(input())

if x-1<=a<=x+1:
    if y-1<=b<=y+1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')