print('구구단')

def gugudan(target: int):
    source= 1
    while source <= 9:
        print(str(target) + ' * ' + str(source) + ' = ' + str(target * source))
        source += 1


number = 2
while number <= 9:
    gugudan(number)
    number += 1