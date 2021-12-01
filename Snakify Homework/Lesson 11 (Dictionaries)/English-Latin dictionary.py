# method A
n = int(input())
mydict = {}
for i in range(n):
    e, l = input().split(' - ')
    l = l.split(', ')
    for i in l:
        mydict[i] = mydict.get(i, []) + [e]

print(len(mydict))
for i in sorted(mydict.keys()):
    print(i, '-', mydict[i][0], end='')
    for j in mydict[i][1:]:
        print(', ', j, sep='', end='')
    print()

# method B
n = int(input())
mydict = {}
for i in range(n):
    eng, latins = input().split(' - ')
    latins = latins.split(', ')
    for latin in latins:
        mydict[latin] = mydict.get(latin, []) + [eng]

print(len(mydict))
for latin in sorted(mydict.keys()):
    print(latin, '-', ', '.join(mydict[latin]))