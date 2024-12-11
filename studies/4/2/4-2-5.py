score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]

print(score)


def parse_stem_leaf(array: []):
    result = []
    for element in array:
        element_str = str(element)
        lastElement = element_str[len(element_str) - 1]
        etcElement = element_str[:-1]
        if etcElement == '':
            etcElement = 0
        if len(result) < int(etcElement) + 1: result.append([])
        result[int(etcElement)].append(int(lastElement))
    return result


print(parse_stem_leaf(score))


def print_pretty(array: list[list]):
    for elementArray in array:
        index = array.index(elementArray)
        print(str(index) + ":", list(elementArray))


print_pretty(parse_stem_leaf(score))
