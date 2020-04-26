def solution(people, limit):
    people = sorted(people, reverse=True)
    start = 0
    end = len(people) - 1
    counter = 0
    while start <= end:
        weight_heavy = people[start]
        weight_light = people[end]
        if weight_heavy + weight_light <= limit:
            end -= 1
        start += 1
        counter += 1
    return counter


if __name__ == '__main__':
    assert solution([70, 50, 80, 50], 100) == 3
    assert solution([70, 80, 50], 100) == 3
