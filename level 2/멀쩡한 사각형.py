def calculate_gcd(a, b):
    if b == 0:
        return a
    return calculate_gcd(b, a % b)


def solution(w, h):
    gcd = calculate_gcd(max(w, h), min(w, h))
    return (w * h) - (w // gcd + h // gcd - 1) * gcd


assert solution(8, 12) == 80
