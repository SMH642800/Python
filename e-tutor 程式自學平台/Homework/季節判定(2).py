def vocation_season(list_month: list[str], dict_m: dict):
    season = set(('Spring', 'Summer', 'Autumn', 'Winter'))
    job_season = set()
    for month in list_month:
        if dict_m[month] not in job_season:
            job_season.add(dict_m[month])
    if len(season-job_season) == 0:
        return 'No'
    else:
        return ' '.join(str(s) for s in season-job_season)


def main():
    list_month = [m for m in input().split()]
    dict_m = {
        '1': 'Winter', '2': 'Winter', '3': 'Spring',
        '4': 'Spring', '5': 'Spring', '6': 'Summer',
        '7': 'Summer', '8': 'Summer', '9': 'Autumn',
        '10': 'Autumn', '11': 'Autumn', '12': 'Winter'
    }

    answer = vocation_season(
        list_month = list_month,
        dict_m = dict_m
    )
    print(answer)


if __name__ == "__main__":
    main()