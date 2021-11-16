m = [int(e) for e in input().split()]
Season_out = []
for i in range(len(m)):
    if 3<=m[i]<=5:
        Season_out.append('Spring')
    elif 6<=m[i]<=8:
        Season_out.append('Summer')
    elif 9<=m[i]<=11:
        Season_out.append('Autumn')
    elif m[i]==12 or 1<=m[i]<=2:
        Season_out.append('Winter')
print(' '.join(Season_out))