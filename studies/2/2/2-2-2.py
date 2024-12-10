print('나이 세대 구분\n')
birthYear = int(input('출생 연도 입력 : '))

if birthYear <= 1924 : print('The Greatest Generation')
elif birthYear <= 1945 : print('The Silent Generation')
elif birthYear <= 1964 : print('baby boomer')
elif birthYear <= 1980 : print('Generation X')
elif birthYear <= 1996 : print('millennial')
else : print('Generation Z')