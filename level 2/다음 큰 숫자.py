def solution(n):
    target = str(bin(n)).count('1')
    m = n + 1
    while str(bin(m)).count('1') != target:
        m += 1
    return m


if __name__ == '__main__':
    assert solution(78) == 83
    assert solution(15) == 23