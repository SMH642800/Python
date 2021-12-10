n = int(input())
mydict = {}
for i in range(n):
    line = input().split()
    for w in line:
        mydict[w] = mydict.get(w, 0) + 1
freqs = [(-c,w) for (w,c) in mydict.items()]
for c,w in sorted(freqs):
    print(w)