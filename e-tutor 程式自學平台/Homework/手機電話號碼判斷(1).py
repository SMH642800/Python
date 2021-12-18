import re
phone_number_regex = re.compile(r'(\d\d\d\d)-(\d\d\d)-(\d\d\d)')


def is_phone_number(phone_number: str):
    if len(phone_number) != 12:
        return 'No'
    else:
        result = phone_number_regex.findall(phone_number)
        if result:
            return phone_number
        else:
            return 'No'


def main():
    phone_number = input()
    print(is_phone_number(phone_number))


if __name__ == "__main__":
    main()