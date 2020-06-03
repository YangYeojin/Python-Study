def solution(N, M):
    answer = 0
    for i in range(len(M)*2):
        if i % 2 == 0:
            answer += sum(N[M[int(i/2)][0]-1:len(N)])
        else:
            answer -= sum(N[M[int(i/2)][1]:len(N)])
    return answer

print(solution([10, 20, 30, 40, 50], [[1, 3], [2, 5], [3, 4], [4, 5]]))

