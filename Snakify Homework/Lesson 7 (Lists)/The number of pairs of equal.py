list_A=[int(i) for i in input().split()]
size_A=len(list_A)
count=0
for i in range(0,size_A):
    for j in range(i+1,size_A):
        if list_A[i] == list_A[j] :
            count+=1
print(count)