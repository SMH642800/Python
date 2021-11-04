x=input().split()
list_A=[int(i) for i in x]
for i in range(1, len(list_A)):
    if list_A[i]*list_A[i-1] > 0:
        print(list_A[i-1], list_A[i], sep=' ')
        break