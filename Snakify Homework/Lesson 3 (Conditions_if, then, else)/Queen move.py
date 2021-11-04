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

if i==j:
    print('YES')
else:
    if a==x or b==y:
        print('YES')
    else:
        print('NO')