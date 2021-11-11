h1, m1 = [int(e) for e in input().split()]
h2, m2 = [int(e) for e in input().split()]
if h1 < h2:
    t = (h2 * 60 + m2)-(h1 * 60 + m1)
elif h1 > h2:
    t = 24*60-(h1 * 60 + m1)+(h2 * 60 + m2)
if t < 150:
    print((t)//30*30)
elif 150 <= t < 240:
    print(120+((t-120)//30*40))
elif t > 240:
    print(120+160+((t-240)//30*60))