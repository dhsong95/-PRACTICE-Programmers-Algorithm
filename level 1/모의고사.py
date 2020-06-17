def solution(answers):
    # 수포자들의 찍는 패턴 리스트
    patterns = [[1, 2, 3, 4, 5],
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    # 수포자들이 맞힌 정답 수
    scores = [0, 0, 0]

    # 문제의 번호(num)와 정답(answer)을 반복
    for num, answer in enumerate(answers):
        for student, pattern in enumerate(patterns):
            pattern_length = len(pattern)
            # 패턴은 반복되므로 modulo 연산 사용
            if pattern[num % pattern_length] == answer:
                scores[student] += 1

    # 최고 성적
    max_score = max(scores)

    # 최고의 성적을 받은 학생 리스트
    students = list()

    for student, score in enumerate(scores):
        if score == max_score:
            # 학생은 1번 학생부터 시작
            students.append(student + 1)

    return students


if __name__ == '__main__':
    assert solution([1, 2, 3, 4, 5]) == [1]
    assert solution([1, 3, 2, 4, 2]) == [1, 2, 3]
