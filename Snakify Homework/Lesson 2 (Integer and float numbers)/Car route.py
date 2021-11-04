N=int(input())
M=int(input())
D=M/N
if (D%1)==0:
    print(int(D))
else:
    print(int(D)+1)