newjins = ['철수', '영희', '민수', '지현', '서연']
ive = ['영희', '민수', '지수', '서연', '하나']
aspa = ['철수', '지현', '지수', '서연', '나영']

result = []
for newjins_fan in newjins:
    if newjins_fan in ive:
        if newjins_fan not in aspa:
            result.append(newjins_fan)

print(list(result))