def solution(N, M):
    answer = 0
    for i in range(len(M)*2):
        if i % 2 == 0:
            answer += sum(N[M[int(i/2)][0]-1:len(N)])
        else:
            answer -= sum(N[M[int(i/2)][1]:len(N)])
    return answer
# sum이 O(n)이 돌아간다고 해서 안 됨...

def solution2(N, M):
    answer = 0
    temp1 = []
    temp2 = []
    for i in range(len(M)*2):
        if i % 2 == 0:
            temp1 += N[M[int(i/2)][0]-1:len(N)]
        else:
            temp2 += N[M[int(i/2)][1]:len(N)]
    answer = sum(temp1) - sum(temp2)
    return answer
# 이렇게 하면 3n인가?

def solution3(N, M):
    answer = []
    for i in range(len(M)):
        answer += N[M[int(i)][0]-1:M[int(i)][1]]
    return sum(answer)
# 이러면 O(M+?) ???

print(solution([10, 20, 30, 40, 50], [[1, 3], [2, 5], [3, 4], [4, 5]]))
print(solution2([10, 20, 30, 40, 50], [[1, 3], [2, 5], [3, 4], [4, 5]]))
print(solution3([10, 20, 30, 40, 50], [[1, 3], [2, 5], [3, 4], [4, 5]]))
