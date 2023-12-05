import random


def karatsuba(x, y):
    if (x < 10) or (y < 10):
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    h1, l1 = divmod(x, 10 ** m)
    h2, l2 = divmod(y, 10 ** m)

    X = karatsuba(h1, h2)
    Y = karatsuba(l1, l2)
    Z = karatsuba((h1 + l1), (h2 + l2)) - X - Y

    return (X * 10 ** (2 * m)) + (Z * 10 ** m) + Y


num_bits = 300
n1 = random.getrandbits(num_bits)
n2 = random.getrandbits(num_bits)

result_standard = n1 * n2
result_karatsuba = karatsuba(n1, n2)

print(f"Standardowe mnożenie: {result_standard}")
print(f"Mnożenie Karatsuby: {result_karatsuba}")
print(f"Poprawne wyniki? {result_standard == result_karatsuba}")
