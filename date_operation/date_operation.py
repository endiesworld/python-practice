from datetime import datetime, timedelta

birthday = input('Please enter you birthday in this format (dd/mm/yyyy): ')

today = datetime.now()

# Convert to datetime data type
try:
    birthday = datetime.strptime(birthday, '%d/%m/%Y')
    birthday_day = birthday.day
    birthday_month = birthday.month
    today_day = today.day
    today_month = today.month

    if birthday_month < today_month:
        birthday_year = today.year + 1
    elif (birthday_month == today_month) & (birthday_day < today_day):
        birthday_year = today.year + 1
    else:
        birthday_year = today.year

    next_celebration = '{}/{}/{}'.format(str(birthday_day),
                                         str(birthday_month), str(birthday_year))
    next_celebration = datetime.strptime(next_celebration, '%d/%m/%Y')
    numbers_of_days = str((next_celebration - today).days)
    print('You have {} days to your next birthday'.format(numbers_of_days))

except ValueError as e:
    print('You have entered the wrong date format')
finally:
    print('Please run the programe again and use the right date format')
