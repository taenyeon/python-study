def parse_date(target_day):
    if target_day < 10: return '0' + str(target_day)
    return str(target_day)


year, month, day = map(lambda element: int(element), input('날짜 입력 : ').split())

print(parse_date(month) + "/" + parse_date(day) + "/" + str(year))

lastDayOfMonth = 30 if month % 2 or month == 8 else 31

day += 1
if day >= lastDayOfMonth:
    if month != 12:
        month += 1
    else:
        year += 1
        month = 1
    day = 1
print(parse_date(month) + "/" + parse_date(day) + "/" + str(year))
