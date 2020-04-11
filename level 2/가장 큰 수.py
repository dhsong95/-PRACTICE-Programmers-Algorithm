def compare(num1, num2):
    return 0 if num1 == num2 else (1 if num1 + num2 > num2 + num1 else -1)


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    left_idx = 0
    right_idx = 0

    merged = list()
    while left_idx < len(left) and right_idx < len(right):
        left_item = left[left_idx]
        right_item = right[right_idx]

        if compare(left_item, right_item) > 0:
            left_idx += 1
            merged.append(left_item)
        else:
            right_idx += 1
            merged.append(right_item)

    while left_idx < len(left):
        left_item = left[left_idx]
        merged.append(left_item)
        left_idx += 1
    while right_idx < len(right):
        right_item = right[right_idx]
        merged.append(right_item)
        right_idx += 1

    return merged


def solution(numbers):
    numbers = [str(num) for num in numbers]
    numbers = merge_sort(numbers)
    return ''.join(numbers) if not numbers[0] == '0' else '0'


assert solution([6, 10, 2]) == '6210'
