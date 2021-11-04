a=int(input())
b=int(input())
c=int(input())

if a==b:
    if a==c:
        print('3')
    else:
        print('2')
elif a==c:
    print('2')
elif b==c:
    print('2')
else:
    print('0')