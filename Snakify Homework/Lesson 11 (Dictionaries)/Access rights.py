n = int(input())
permission = {}
for i in range(n):
    line = input().split()
    permission[line[0]] = line[1:]

action = {'write':'W', 'read':'R', 'execute':'X'}
q = int(input())
for i in range(q):
    a, file = input().split()
    if action[a] in permission[file]:
        print('OK')
    else:
        print('Access denied')