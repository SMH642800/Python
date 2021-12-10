n = int(input())
students = [{input() for j in range(int(input()))} for i in range(int(input()))]
same, all = set.intersection(*students), set.union(*students)
print(len(same))
for i in same:
    print(i)
print(len(all))
for i in sorted(all):
    print(i)
    
'''
students = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
print(len(known_by_someone), *sorted(known_by_someone), sep='\n')
'''