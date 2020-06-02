import itertools


def solution_hash(phone_book, h=True):
    # 해시를 사용한 풀이
    if h:
        hash_table = {phone_number:1 for phone_number in phone_book}

        for phone_number in phone_book:
            prefix = ''
            # 전화번호에서 마지막 글자만을 제외하고 접두사를 구한다. (ex, 119 -> 1, 11)
            for number in phone_number[:-1]:
                prefix += number
                # 접두사가 해시 테이블의 키에 있다면 접두사 관계의 전화 번호가 있는 것이다.
                if prefix in hash_table.keys():
                    return False

        return True
    # 해시를 사용하지 않은 풀이
    else:
        # itertools 라이브러이에서 조합을 구하는 메서드 combinations 사용. 2개의 전화번호를 구한다
        for p1, p2 in itertools.combinations(phone_book, 2):
            # 전화번호가 접두사 관계인지 파악한다.
            if p1.startswith(p2) or p2.startswith(p1):
                return False
        return True


def solution(phone_book):
    # 해시를 사용한 풀이
    answer_h = solution_hash(phone_book)

    # 해시를 사용하지 않은 풀이
    answer_nh = solution_hash(phone_book, False)

    assert answer_h == answer_nh

    return answer_h


if __name__ == '__main__':
    assert not solution(['119', '97674223', '1195524421'])
    assert solution(['123', '456', '789'])
    assert not solution(['12', '123', '1235', '567', '88'])


