import re
from collections import Counter


def solution(s):
    counter = Counter(re.findall(r'\d+', s))
    return [int(num[0]) for num in counter.most_common()]


if __name__ == '__main__':
    assert solution('{{2},{2,1},{2,1,3},{2,1,3,4}}') == [2, 1, 3, 4]
