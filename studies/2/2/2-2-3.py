print('단위 기호 (k)')

inputNumber = int(input('입력 : '))
result = str(inputNumber)
if inputNumber >= 1000:
    result = str(inputNumber // 1000) + 'k'
elif inputNumber >= 0:
    pass

print(result)
