# Uses python3


def gcd(a, b):
    if b == 0:
        return a
    rem = int(int(a) % int(b))
    if rem == 0:
        return b
    return gcd(b, rem)


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


a, b = map(int, input().split())
print(a * b // gcd(a, b))
