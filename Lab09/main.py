import math


# Silnia
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Symbol Newtona
# z definicji
def binomial_coefficient_definition(n, k):
    if k < 0 or k > n:
        return 0
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


# rekurencyjnie
def binomial_coefficient_recursive(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_coefficient_recursive(n - 1, k - 1) + binomial_coefficient_recursive(n - 1, k)


# iteracyjnie
def binomial_coefficient_iterative(n, k):
    if k < 0 or k > n:
        return 0

    result = 1
    for i in range(1, k + 1):
        result *= (n - i + 1)
        result //= i

    return result


# Liczby Stirlinga II rodzaju
# rekurencyjnie
def stirling_recursive(n, k):
    if k == 0 or n == 0 or k > n:
        return 0
    if k == n:
        return 1
    return k * stirling_recursive(n - 1, k) + stirling_recursive(n - 1, k - 1)


# używając wzoru
def stirling_formula(n, k):
    if k == 0 or n == 0 or k > n:
        return 0

    result = 0
    for j in range(k + 1):
        result += (-1) ** (k - j) * math.comb(k, j) * (j ** n)

    return result // math.factorial(k)


# Liczby Bella
# ze wzoru rekurencyjnego
def bell_recursive(n):
    if n == 0:
        return 1

    bell = [0] * (n + 1)
    bell[0] = 1

    for i in range(1, n + 1):
        for k in range(i):
            bell[i] += math.comb(i - 1, k) * bell[k]

    return bell[n]


# z użyciem liczb Stirlinga 2 rodzaju
def bell_stirling(n):
    result = 0
    for k in range(n + 1):
        result += stirling_recursive(n, k)

    return result

# Liczba podzialow n na k skladnikow to Stirling II rodzaju
