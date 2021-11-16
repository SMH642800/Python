while True:  
  try:        
    n = int(input())
    a = [int(e) for e in input().split()]
    s = []
    d = []
    for i in range(2*n):
        if i%2 == 0:
            s.append(a[i])
        else:
            d.append(a[i])
    for i in range(n):
        d[i] += 1

    car_num = n
    for j in range(n):
        for i in range(j+1,n):
            if d[j] <= s[i]:
                car_num -= 1
                break
    print(car_num)
  except (EOFError):  
    break  
