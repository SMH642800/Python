n = int(input())
mydict = {}
for e in range(n):
    name, votes = input().split()
    mydict[name] = mydict.get(name, 0) + int(votes)

for name in sorted(mydict.keys()):
    print(name, mydict[name])