while True:  
  try:        
    s = input()
    d = {}
    for i in s.split():
        d[i] = d.get(i,0)+1

    for i,j in d.items():
        print(i)
        print(j)
        if j > len(s.split())/2:
            print(i)
            break
    else:
        print('NO')
  except (EOFError):  
    break  
