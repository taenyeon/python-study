def prime_number(max_range):
    numbers = list(range(2, max_range))
    index = 0
    while index < len(numbers):
        num = numbers[index]
        numbers = list(filter(lambda x: x == num or x % num, numbers))
        index += 1
    return numbers

print(prime_number(50))
