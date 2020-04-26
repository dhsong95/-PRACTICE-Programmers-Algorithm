def solution(n):
    fibonacci = [0, 1]
    idx = 2
    while idx <= n:
        num = (fibonacci[-1] + fibonacci[-2]) % 1234567
        fibonacci.append(num)
        idx += 1
    return fibonacci[-1]


if __name__ == '__main__':
    assert solution(3) == 2
    assert solution(5) == 5
