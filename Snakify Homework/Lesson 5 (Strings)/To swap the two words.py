word_list = input().split()
word_list[0], word_list[1] = word_list[1], word_list[0]
print(' '.join(word_list))