print('윤년 체크\n')

year = int(input('년도 입력 : '))
result = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0: result = True
    else:
        result = True

if result:
    print(str(year) + '년은 윤년')
else:
    print(str(year) + '년은 평년')
