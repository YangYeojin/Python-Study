'''
def solution(scoville, K):
    answer = 0
    scoville = sorted(scoville)

    while True:
        # 두 음식을 섞는 부분
        if scoville[0] < K:
            new_scoville = [scoville[0] + scoville[1] * 2]
            scoville = new_scoville + scoville[2:]
            answer += 1

        # 배열을 재정렬하는 부분
        if len(scoville) == 1:
            if scoville[0] >= K:
                return answer
            else:
                return -1
        if scoville[0] > scoville[1]:
            for j in range(len(scoville)+1):
                if scoville[0] >= scoville[-1]:
                    scoville = scoville[1:] + [scoville[0]]
                    break
                if scoville[0] < scoville[j] or scoville[j] > K:
                    scoville = scoville[1:j] + [scoville[0]] + scoville[j:]
                    break
        if scoville[0] < scoville[1] and K <= scoville[0]:
            return answer
    return answer
# 시간초과 남 - 배열 재정렬 부분이 문제인 듯
'''

# 내가 heap을 상당히 잘 못 썼나보다 다시 공부해야겠다 하고 구글 검색하다가 heapq라는 모듈을 발견함
# 나는 heap을 내가 구현해야 하는 줄 알고 아이고 귀찮다 대충 해보자 했지...
# 신난다 모듈을 씁시다 이히히
import heapq

def solution(scoville, K):
    answer = 0
    i = 0
    heapq.heapify(scoville)
    while scoville[0] <= K:
        if len(scoville) == 1:
            return -1
        heapMin = heapq.heappop(scoville)
        heapq.heappush(scoville, heapMin + heapq.heappop(scoville) * 2)
        answer += 1
    return answer

print(solution([1,1,2,3],20))
print(solution([1,2,3,9,10,12], 7))