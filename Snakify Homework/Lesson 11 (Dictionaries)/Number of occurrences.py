mydict = {}
for w in input().split():
    print(mydict.get(w,0), end=' ')
    mydict[w] = mydict.get(w, 0) + 1