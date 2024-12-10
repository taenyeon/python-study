def simple_interest(p, r, t):
    return p * r * t


def simple_interest_amount(p, r, t):
    return p * (1 + r * t)


print(simple_interest(10000000, 0.03875, 5))

print(simple_interest_amount(10000000, 0.03875, 5))
