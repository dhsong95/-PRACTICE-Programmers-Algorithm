"""
Better Using Index rather than append/pop for Time Efficiency
"""


def solution(number, k):
    number_stack = [number[0]]
    idx = 1

    while idx < len(number) and k > 0:
        top = number_stack[-1]
        num = number[idx]

        while number_stack and top < num and k > 0:
            number_stack.pop(-1)
            k -= 1
            if number_stack:
                top = number_stack[-1]

        number_stack.append(num)
        idx += 1

    if k == 0:
        return ''.join(number_stack) + number[idx:]
    else:
        return ''.join(number_stack[:-k])


if __name__ == '__main__':
    assert solution('1924', 2) == '94'
    assert solution('1231234', 3) == '3234'
    assert solution('4177252841', 4) == '775841'
