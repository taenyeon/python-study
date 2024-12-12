from functools import reduce

inputNumbers = list(map(lambda element: int(element), input('여러 수 입력 : ').split()))

addition = reduce(lambda a, b: a + b, inputNumbers)
subtraction = reduce(lambda a, b: a - b, inputNumbers)
multiplication = reduce(lambda a, b: a * b, inputNumbers)
division = reduce(lambda a, b: a / b, inputNumbers)

print(addition, subtraction, multiplication, division)
