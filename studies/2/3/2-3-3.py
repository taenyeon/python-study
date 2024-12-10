from typing import List

print('화학 실험실')
inputNumbers: list[str] = str(input('최소값/최대값 입력 : ')).split(' ')  # "최소값 최대값" ex) "10 20"

min: int = int(inputNumbers[0])
max: int = int(inputNumbers[1])

inputNumbers = str(input('상태 입력 : ')).split(' ')  # ex) 15 10 20 0 15 -999

for number in inputNumbers:
    if min <= int(number) <= max:
        print('Nothing to report')
    elif int(number) == -999:
        break
    else:
        print('Alert!')
        break
