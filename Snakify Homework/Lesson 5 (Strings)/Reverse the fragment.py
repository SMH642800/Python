s = input()
p1 = s.find('h')
p2 = s.rfind('h')
s1 = s[:p1+1]
s2 = s[p2-1:p1:-1]
s3 = s[p2:]
print(s1+s2+s3)
