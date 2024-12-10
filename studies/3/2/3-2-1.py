def korean_number(number):
    return {1: '일',
            2: '이',
            3: '삼',
            4: '사',
            5: '오',
            6: '육',
            7: '칠',
            8: '팔',
            9: '구',
            10: '십',
            }.get(number, 'notFound')


print(korean_number(1))
print(korean_number(10))
print(korean_number(11))