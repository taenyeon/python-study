def sum_of_digits(num: int):
    array = list(str(num))
    return sum(map(lambda x: int(x), array))


print(sum_of_digits(99))
print(sum_of_digits(643))
print(sum_of_digits(47253))