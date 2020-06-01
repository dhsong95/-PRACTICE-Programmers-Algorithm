def solution(participant, completion):
    table = {p: 0 for p in set(participant)}

    # 등장횟수 + 1
    for p in participant:
        table[p] += 1
    # 등장횟수 - 1
    for p in completion:
        table[p] -= 1

    for k, v in table.items():
        if v == 1:
            return k


if __name__ == '__main__':
    assert solution(["leo", "kiki", "eden"], ["eden", "kiki"]) == "leo"
    assert solution(["marina", "josipa", "nikola", "vinko", "filipa"],
                    ["josipa", "filipa", "marina", "nikola"]) == "vinko"
    assert solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]) == "mislav"
