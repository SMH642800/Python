num = int(input())
even_num_count = 0
while num != 0:
    if num%2 == 0:
        even_num_count += 1
    num = int(input())
print(even_num_count)