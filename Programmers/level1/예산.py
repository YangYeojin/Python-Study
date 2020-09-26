# 풀이방법 예상 : sort(d) <- 오름차순 후 list[]를 처음부터 하나하나 더해 'budget'와 크기 비교, 'budget'이 더 작아지면 break

def solution(d, budget):
    answer = 0
    if sum(d) <= budget:
        return len(d)
    else:
        d.sort()
        supportSum = 0  # 지금까지 다른 부서에 지원되기로 할당된 금액의 합
        while supportSum+d[answer] <= budget:
            supportSum += d[answer]
            answer += 1
        return answer

print("answer:", solution([1,3,2,5,4], 9))
print("-"*20)
print("answer:", solution([2,2,3,3], 20))