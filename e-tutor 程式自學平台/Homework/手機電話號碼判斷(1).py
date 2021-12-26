import re
phone_number_regex = re.compile(r'(\d\d\d\d)-(\d\d\d)-(\d\d\d)')   #正規表達式，建立尋找條件


def is_phone_number(phone_number: str):
    if len(phone_number) != 12:   #長度是否等於12
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
