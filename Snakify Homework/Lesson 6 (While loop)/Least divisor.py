#while loop version
n = int(input())
i=2
while n%2 !=0:
    i += 1
print(i)

#for loop version
n = int(input())
for i in range(2,n+1):
    if n%i == 0:
        print(i)
        break

