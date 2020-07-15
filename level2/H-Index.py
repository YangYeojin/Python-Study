def solution(citations):
    citations = sorted(citations)
    for h in range(len(citations)):
        print(citations[h], len(citations) - h)
        if citations[h] >= len(citations) - h:
            return len(citations) - h
    return 0

print(solution([10, 13, 0, 16, 1, 15]))