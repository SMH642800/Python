x = int(input())  
    count = 0  
    for i in range(2,x//2+1):  
        if x%i == 0:  
            count+=1  
    if count > 0:  
        print('NO')  
    else:  
        print('YES')