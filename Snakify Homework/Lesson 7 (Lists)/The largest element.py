x=input().split()
list_A=[int(i) for i in x]
num_max=list_A[0]
for i in list_A:
    if num_max<i:
        num_max=i
print(num_max, list_A.index(num_max), sep=' ')
