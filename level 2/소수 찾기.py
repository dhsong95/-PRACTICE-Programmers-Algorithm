from itertools import permutations


def determine_prime(number):
    # 0과 1은 소수가 아니다
    if number in [0, 1]:
        return False

    # 2부터 숫자의 제곱근까지 반복하여서 나누어떨어지는지 확인
    for n in range(2, int(number ** 0.5) + 1):
        # 나누어떨어지므로 소수가 아니다
        if number % n == 0:
            return False
    return True


def find_candidates(numbers):
    # numbers 의 자릿수 length
    length = len(numbers)

    # set 자료구조는 중복을 허용하지 않는다.
    candidates = set()

    # 한 자릿수부터 N 자릿수까지 가능한 모든 순열 파악하기
    for n in range(1, length + 1):
        # permutations() 는 리스트의 원소에 대해서 n 개의 순열을 구해준다.
        # ''로 묶은 이후에 int 로 형변환하여서 0이 아니면서 0으로 시작하는 숫자를 제거한다
        for candidate in map(lambda x: int(''.join(x)), permutations(numbers, n)):
            candidates.add(candidate)

    return candidates


def solution(numbers):
    # 각 자리수의 리스트로 만들기
    numbers = [num for num in numbers]

    candidates = find_candidates(numbers)

    counter = 0
    for candidate in candidates:
        counter += int(determine_prime(candidate))

    return counter


if __name__ == '__main__':
    assert solution('17') == 3
    assert solution('011') == 2
