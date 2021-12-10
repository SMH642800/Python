n = int(input())
a = set([int(i) for i in range(1, n+1)])
inp = input()
while inp != 'HELP':
    line = set([int(e) for e in inp.split()])
    ans = input()
    if ans == 'YES':
        a = a&line
    elif ans == 'NO':
        a = a-line
    inp = input()
for i in sorted(list(a)):
    print(i, end=' ')