import re
phone_number_rule = re.compile(r'(\(\d{2}\))(\d{3}-\d{4})(\s|\W|\Z)')


def is_phone_number(sentence: str):
    result = phone_number_rule.search(sentence)
    if result:
        return result.group(2)
    else:
        return 'No'


def main():
    sentence = input()
    print(is_phone_number(sentence))


if __name__ == "__main__":
    main()