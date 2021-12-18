def is_same_season(list_month: list[str], dict_m: dict, first_season: str) -> str:
    for i in range(1, len(list_month)):
        second_season = dict_m[list_month[i]]
        if second_season != first_season:
            return 'No'
    return first_season


def main():
    list_month = [m for m in input().split()]
    dict_m = {
        '1': 'Winter', '2': 'Winter', '3': 'Spring',
        '4': 'Spring', '5': 'Spring', '6': 'Summer',
        '7': 'Summer', '8': 'Summer', '9': 'Autumn',
        '10': 'Autumn', '11': 'Autumn', '12': 'Winter'
    }

    first_season = dict_m[list_month[0]]
    answer = is_same_season(
        list_month = list_month,
        dict_m = dict_m,
        first_season = first_season
    )
    print(answer)


if __name__ == "__main__":
    main()
