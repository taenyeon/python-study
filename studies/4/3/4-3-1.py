def operations_result(target, source):
    return target + source, target - source, target * source, target / source


target, source = map(lambda x : int(x), input("두 수 입력").split())

print(operations_result(target, source))
