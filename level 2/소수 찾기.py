import itertools


def prime(number):
    if number <= 1:
        return False

    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
    return True


def solution(numbers):
    numbers = [number for number in numbers]
    candidates = set()
    for length in range(1, len(numbers) + 1):
        permutations = itertools.permutations(numbers, length)
        for permutation in permutations:
            if permutation[0] != '0':
                candidates.add(int(''.join(permutation)))

    counter = 0
    for candidate in candidates:
        counter += (1 if prime(candidate) else 0)

    return counter


if __name__ == '__main__':
    assert solution('17') == 3
    assert solution('011') == 2
