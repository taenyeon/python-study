def hap(x, y):
    return x + y


print(hap(10, 20))

print((lambda x, y: x + y)(10, 20))


# map
def square(range_number):
    startNumber = 0
    result = []
    while startNumber < range_number:
        result.append(startNumber ** 2)
        startNumber += 1
    return result


print(square(5))

print(list(map(lambda x: x ** 2, range(5))))

# reduce

from functools import reduce


def reduce_fun(array: []):
    result = None
    for element in array:
        if result is None:
            result = element
        else:
            result += element
    return result


print(reduce_fun([0, 1, 2, 3, 4]))
print(reduce_fun('abcde'))

print(reduce(lambda x, y: x + y, [0, 1, 2, 3, 4]))
print(reduce(lambda x, y: y + x, 'abcde'))

# filter
print(list(filter(lambda x: x < 5, range(10))))
print(list(filter(lambda x: x % 2, range(10))))
