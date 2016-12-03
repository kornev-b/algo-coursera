# Uses python3


def get_change(m):
    tens = m // 10
    rem = m % 10
    if rem == 0:
        return tens
    fives = rem // 5
    rem %= 5
    if rem == 0:
        return tens + fives
    return tens + fives + rem


while True:
    m = int(input())
    print(get_change(m))
