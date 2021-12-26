def sorted_input_date(numbers_of_lines: int, ans: list):
    for i in range(numbers_of_lines):      # 共有N行輸入
        set_of_point = []                  # 建立一個list來儲存所有point的資料集合
        line = input().split()
        numbers_of_points = int(line[0])   # 每行的第一個數字代表多少個points
        x_of_first_point = int(line[1])    # 每行第一個point的X座標
        y_of_first_point = int(line[2])    # 每行第一個point的Y座標
        for j in range(0, numbers_of_points*2, 2):
            point = [0 for _ in range(3)]  # 建立一個list來儲存每一個point的 [x, y, 距離第一個point的距離]
            x = int(line[j+1])
            y = int(line[j+2])
            distance = (x - x_of_first_point) ** 2 + (y - y_of_first_point) ** 2
            point[0] = x
            point[1] = y
            point[2] = distance
            set_of_point.append(point)      # 把 point [x, y, 距離第一個point的距離] 儲存至set of point裡
        sorted_ans = sorted(set_of_point, key=lambda x: (x[2], x[0]), reverse = True)  # 距離由大至小排序，若距離相同，x座標較大者先
        ans.append(sorted_ans)      # 把每行的所有已排序好的point資料儲存至ans裡
    return ans      # 回傳以排序好的ans


def print_ans(numbers_of_lines: int, ans: list):
    for i in range(numbers_of_lines):
        n = len(ans[i])
        for j in range(n):
            if j == n - 1:      # 當j讀取到最後一組資料時，手動進行輸出，並在輸出完最後一個元素時馬上換行
                print(ans[i][j][0], end=' ')
                print(ans[i][j][1])
            else:
                for k in range(2):
                    print(ans[i][j][k], end=' ')


def main():
    numbers_of_lines = int(input())
    ans = []
    sorted_input_date(numbers_of_lines, ans)   # 把input資料進行排序
    print_ans(numbers_of_lines, ans)           # 把排序完的資料print出來


if __name__ == "__main__":
    main()