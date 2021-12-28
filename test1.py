while True:  
  try:
    numbers_of_lines = int(input())
    ans = []
    for i in range(numbers_of_lines):   #共有N行輸入
        set_of_point = []
        line = input().split()
        numbers_of_points = int(line[0])
        x_of_first_point = int(line[1])
        y_of_first_point = int(line[2])
        for j in range(0, numbers_of_points*2, 2):
            point = [0 for _ in range(3)]
            x = int(line[j+1])
            y = int(line[j+2])
            distance = (x-x_of_first_point)**2 + (y-y_of_first_point)**2
            point[0] = x
            point[1] = y
            point[2] = distance
            set_of_point.append(point)
        sorted_ans = sorted(set_of_point, key=lambda x: (x[2], x[0]), reverse = True)
        ans.append(sorted_ans)
    for i in range(numbers_of_lines):
        n = len(ans[i])
        for j in range(n):
            if j == n - 1:
                print(ans[i][j][0], end=' ')
                print(ans[i][j][1])
            else:
                for k in range(2):
                    print(ans[i][j][k], end=' ')
  except (EOFError):  
    break  
