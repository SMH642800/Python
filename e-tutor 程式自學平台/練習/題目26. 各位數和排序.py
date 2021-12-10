n = input()
n = [int(e) for e in input().split()]
l = sorted(n, key=lambda x:(sum([int(i) for i in str(x)]), x))
ret = ' '.join([str(i) for i in l])
print(ret)