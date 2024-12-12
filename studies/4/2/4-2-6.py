def sum_of_digits(num):
    return sum(map(lambda x: int(x), list(str(num))))


print(sum_of_digits(47253))
