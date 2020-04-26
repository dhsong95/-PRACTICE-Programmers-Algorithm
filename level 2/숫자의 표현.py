def solution(n):
    smallest = n
    m = 1
    counter = 0

    while smallest > 0:
        q = n // m
        r = n % m
        if m % 2 == 1:
            if r == 0:
                smallest = q - m // 2
                counter += 1
        else:
            if r == (m // 2):
                smallest = q - r - 1
                counter += 1
        m += 1
        counter -= (1 if smallest <= 0 else 0)
    return counter


if __name__ == '__main__':
    assert solution(15) == 4
