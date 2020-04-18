def solution(citations):
    answer = 0
    for citation in citations:
        more = len([c for c in citations if c >= citation])
        h = more if citation >= more else citation
        answer = h if answer < h else answer

    return answer
