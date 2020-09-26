def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1
    return answer


print("\n", solution([1, 2, 3, 2, 3]))


'''
from collections import deque

def solution(prices):
    answer = list()
    for i in range(len(prices)):
        temp = deque(prices[i+1:])
        while len(temp) != 0:
            a = temp.popleft()
            if a < prices[i]:
                break
        answer += [len(prices[i+1:]) - len(temp)]
    return answer

# 스택/큐 문제여서 'deque'로 풀려고 했는데 시간 초과
'''