n = int(input())
mydict = {}
for i in range(n):
    w1, w2 = input().split()
    mydict[w1] = w2
    mydict[w2] = w1
print(mydict[input()])