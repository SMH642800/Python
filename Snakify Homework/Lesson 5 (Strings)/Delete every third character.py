s = input()
s1 = []
for i in range(len(s)):
    if i%3 != 0:
        s1.append(s[i])
print(''.join(s1))