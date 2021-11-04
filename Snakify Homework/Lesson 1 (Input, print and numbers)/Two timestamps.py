h1=int(input())
m1=int(input())
s1=int(input())
h2=int(input())
m2=int(input())
s2=int(input())

total1=h1*60*60+m1*60+s1
total2=h2*60*60+m2*60+s2

ans=total2-total1

print(ans)