while True:  
  try:  
    x=input().split()
    list_A=[int(i) for i in x]
    for i in list_A[:len(list_A)-1:2]:
        print(i, end=' ')
    print(list_A[len(list_A)-1])
  except (EOFError):  
    break  
