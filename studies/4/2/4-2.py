x = 'banana'

print(x[0])

print(x[2:4])

print(x[:3])

print(x[3:])

x = 'n' + x[1:]

print(x)

s = 'hello Python'

print(s.find('P'))

print(s[0:6])

h = s[0:6]

print(h[0:5])

print(h.rstrip())

print(s.split())
print(s.split()[0])

prime = [3, 7, 11]
prime.append(5)
print(prime)

prime.insert(0, 2)
print(prime)

del prime[4]
print(prime)

a = prime.pop()
print(prime)
print(a)

prime[0] = 1
print(prime)

orders = ['potato', ['pizza', 'Coke', 'salad'], 2]

print(orders[0])
print(orders[1])
print(orders[2])

matrix = [[1, 2, 3], [4, 5, 6, ], [7, 8, 9]]
print(matrix)

characters = []
sentence = 'hello world'
for char in sentence:
    characters.append(char)
print(characters)

print(list('hello world'))

my_int = 123
print(type(my_int))

print(str(my_int))
print(type(str(my_int)))

print(int('123'))
print(float('123'))

one_to_ten = list(range(1, 11))
print(one_to_ten)

print(sum(one_to_ten))

a_man = [90, 85, 70]
b_man = [88, 79, 92]
c_man = [100, 100, 100]
d_man = [90, 60, 70]

students = [a_man, b_man, c_man, d_man]

for scores in students:
    print(scores)

for scores in students:
    total = 0
    for score in scores:
        total += score
    total /= len(scores)
    print(total)
