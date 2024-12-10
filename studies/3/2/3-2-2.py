def triple(x):
    return x ** 3


from datetime import datetime


def korean_age(birth_year):
    _todayYear = datetime.today().year
    return _todayYear - birth_year + 1


print(triple(3))

print(korean_age(1999))
