word = input()
if word.count('f') > 1:
    position1 = word.find('f')
    position2 = word.find('f', position1+1)
    print(position2)
elif word.count('f') == 1:
    print('-1')
else:
    print('-2')
