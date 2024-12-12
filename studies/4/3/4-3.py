a = 10
b = 20
temp = a
a = b
b = temp
print(a, b)

c = 10
d = 20
c, d = d, c
print(c, d)


def magu_print(x, y, *rest, ):
    print(x, y, rest)
    print(type(rest))
    print(rest[0])
    print(list(filter(lambda element: element % 2, rest)))


magu_print(1, 2, 3, 4, 5, 6, 7, 8)

t = ('a', 'b', 'c')
empty = ()
one = 5,
print(one)

p = (1,2,3)
q = p[:1] + (5,) + p[2:]
print(q)

r = p[:1], 5, p[2:]
print(r)