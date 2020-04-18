def solution(clothes):
    clothes_dict = dict()
    for v, k in clothes:
        if k not in clothes_dict.keys():
            clothes_dict[k] = 0
        clothes_dict[k] += 1

    answer = 1
    for v in clothes_dict.values():
        answer *= (v + 1)

    return answer - 1
