def solution(n):
    num_str = str()
    while n:
        r = n % 3 if n % 3 else 4
        num_str += str(r)
        n -= (1 if not n % 3 else 0)
        n //= 3
    return num_str[::-1]


assert solution(6) == '14'
