import re
sentence_rule = re.compile(r'[aA]\w*\d+\w*')   #以A或a為首，且後面字串中包含有至少一個數字，的所有單字


def match(sentence str)
    result = sentence_rule.findall(sentence)
    if result
        return ' '.join(str(i) for i in list(result))
    else
        return 'No'


def main()
    sentence = input()
    print(match(sentence))


if __name__ == __main__
    main()
