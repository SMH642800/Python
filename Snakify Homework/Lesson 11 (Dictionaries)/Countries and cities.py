n = int(input())
mydict = {}
for i in range(n):
    line = input().split()
    for city in line[1:]:
        mydict[city] = line[0]

q = int(input())
for i in range(q):
    print(mydict[input()])