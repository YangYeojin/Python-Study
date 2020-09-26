# 인용된 수가 작은 경우부터 고려하며 인용된 수가 그보다 적게 인용된 논문의 편 수를 넘어가면
# 그보다 적게 인용된 논문의 편 수<len(citations) - h>를 return
# len(citations) - h는 인용된 횟수가 citations[h]보다 크거나 같은 논문의 수를 의미함

def solution(citations):
    citations = sorted(citations)
    for h in range(len(citations)):
        if citations[h] >= len(citations) - h:
            return len(citations) - h
    return 0


solution([10, 13, 0, 16, 1, 15])