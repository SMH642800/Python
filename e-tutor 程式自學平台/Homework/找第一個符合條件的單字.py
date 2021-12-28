import re
sentence_rule = re.compile(r'\d\w*a+\w*\d')   #以數字為首尾，且其中包含至少一個a的所有單字


def compact_rule(sentence: str):
    result = sentence_rule.search(sentence)
    if result:
        return result.group()
    else:
        return 'No'


def main():
    sentence = input()
    print(compact_rule(sentence))


if __name__ == "__main__":
    main()




