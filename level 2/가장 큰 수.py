def compare(a, b):
    return int(a + b) - int(b + a)


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    idx = len(numbers) // 2

    l1 = merge_sort(numbers[:idx])
    l2 = merge_sort(numbers[idx:])

    l3 = list()

    idx = 0
    jdx = 0

    while idx < len(l1) and jdx < len(l2):
        a = l1[idx]
        b = l2[jdx]

        if compare(a, b) > 0:
            l3.append(a)
            idx += 1
        else:
            l3.append(b)
            jdx += 1

    while idx < len(l1):
        l3.append(l1[idx])
        idx += 1

    while jdx < len(l2):
        l3.append(l2[jdx])
        jdx += 1

    return l3


def solution(numbers):
    numbers = [str(num) for num in numbers]
    numbers = merge_sort(numbers)
    return ''.join(numbers) if not numbers[0] == '0' else '0'


if __name__ == '__main__':
    assert solution([6, 10, 2]) == '6210'
