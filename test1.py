while True:  
  try:        
    list_month = [m for m in input().split()]
    dict_m = {
        '1': 'Winter', '2': 'Winter', '3': 'Spring',
        '4': 'Spring', '5': 'Spring', '6': 'Summer',
        '7': 'Summer', '8': 'Summer', '9': 'Autumn',
        '10': 'Autumn', '11': 'Autumn', '12': 'Winter'
    }
    dict_season_order = {
        'Spring': 1, 'Summer': 2, 'Autumn': 3, 'Winter': 4
    }

    season = {'Spring', 'Summer', 'Autumn', 'Winter'}
    job_season = set()
    for month in list_month:
        if dict_m[month] not in job_season:
            job_season.add(dict_m[month])
    if len(season-job_season) == 0:
        print('No')
    else:
        free_season = list(season-job_season)
        list_free_season_order = [dict_season_order[s] for s in free_season]
        answer = [x for _, x in sorted(zip(list_free_season_order, free_season))]
        print(' '.join(answer))
      
  except (EOFError):  
    break  

while True:  
  try:        
    import re
    phone_number_regex = re.compile(r'(\d\d\d\d)-(\d\d\d)-(\d\d\d)')

    phone_number = input()
    if len(phone_number) != 12:
        print('No')
    else:
        result = phone_number_regex.findall(phone_number)
        if result:
            print(phone_number)
        else:
            print('No')
  except (EOFError):  
    break  
