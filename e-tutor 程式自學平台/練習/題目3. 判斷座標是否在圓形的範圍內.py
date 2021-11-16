x, y = [int(e) for e in input().split()]
if abs(x)**2 + abs(y)**2 <= 100**2:
    print('inside')
else:
    print('outside')