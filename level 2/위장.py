def solution(clothes):
    hash_table = dict()
    for _, kind in clothes:
        if kind not in hash_table:
            hash_table[kind] = 0
        hash_table[kind] += 1

    number_of_cases = 1
    for value in hash_table.values():
        number_of_cases *= (value + 1)

    number_of_cases -= 1
    return number_of_cases


if __name__ == '__main__':
    assert solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]) == 5
    assert solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]) == 3
