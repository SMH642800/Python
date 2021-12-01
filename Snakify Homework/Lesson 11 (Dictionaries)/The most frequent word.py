# method A
n = int(input())
mydict = {}
for i in range(n):
    words = input().split()
    for w in words:
        mydict[w] = mydict.get(w, 0) + 1

def cmp(x):
    return -x[1], x[0]
result = sorted(mydict.items(), key=cmp)
print(result[0][0])

# method B
n = int(input())
mydict = {}
for i in range(n):
    words = input().split()
    for w in words:
        mydict[w] = mydict.get(w, 0) + 1

max_count = max(mydict.values())
most_frequent = [k for k in mydict if mydict[k] == max_count]
print(min(most_frequent))