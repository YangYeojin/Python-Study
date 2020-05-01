def solution(x, n):
    answer = []
    # x가  0일 때
    if x == 0 :
        return [0] * n
    # x가 0이 아닐 때
    for i in range(x, x*(n+1), x):
        answer += [i]
    return answer