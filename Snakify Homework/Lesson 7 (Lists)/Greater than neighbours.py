x=input().split()
list_A=[int(i) for i in x]
count=0
for i in range(1, len(list_A)-1):
    if list_A[i-1] < list_A[i] and list_A[i+1] < list_A[i]:
        count+=1
print(count)
