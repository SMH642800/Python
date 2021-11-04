x=int(input())
y=int(input())
a=int(input())
b=int(input())

if x>a:
    x,a=a,x
if y>b:
    y,b=b,y

i=a-x
j=b-y

if i%2==0:
    if j%2==0:
        print('YES')
    else:
        print('NO')
else:
    if j%2==0:
        print('NO')
    else:
        print('YES')