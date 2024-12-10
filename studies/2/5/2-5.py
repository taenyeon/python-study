for number in [1, 2, 3, 4]:
    print(number)
else:
    print('리스트의 원소를 모두 출력했음')

for number in [1, 2, 3, 4]:
    if number % 3:
        print(number)
    else:
        break
else:
    print('리스트의 원소를 모두 출력했음')

countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    if input() == '중단':
        break
else:
    print('발사')
