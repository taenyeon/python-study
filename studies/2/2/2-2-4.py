result = 0

while True:
    inputNumber = int(input('정수 입력 : '))
    if inputNumber >= 0:
        result += inputNumber
    else:
        break
print(result)
