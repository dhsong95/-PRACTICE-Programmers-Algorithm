def solution(s):
    end = len(s) // 2
    answer = len(s)

    for length in range(1, end + 1):
        compressed = ''
        idx = length
        counter = 1
        while idx <= len(s) - length:
            prev_s = s[idx - length: idx]
            next_s = s[idx: idx + length]

            if prev_s == next_s:
                counter += 1
            else:
                if counter == 1:
                    compressed += prev_s
                else:
                    compressed += str(counter) + prev_s
                counter = 1

            idx += length

        if counter == 1:
            compressed += next_s + s[idx:]
        else:
            compressed += str(counter) + prev_s + s[idx:]

        answer = len(compressed) if len(compressed) < answer else answer

    return answer


if __name__ == '__main__':
    assert  solution('aabbaccc') == 7
    assert  solution('ababcdcdababcdcd') == 9
    assert  solution('abcabcdede') == 8
    assert  solution('abcabcabcabcdededededede') == 14
    assert  solution('xababcdcdababcdcd') == 17
