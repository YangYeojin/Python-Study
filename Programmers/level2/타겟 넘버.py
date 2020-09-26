# 깊이 우선 탐색(DFS)을 하든 너비 우선 탐색(BFS)을 하든 차이는 없을 것 같음 => DFS
# 함수가 내부에서 몇 번 반복되어야 하는지 모르겠음
# 함수를 작성하고 를 호출하도록 하는 게 어떨까 (시간 초과 발생 가능성 있음)

answer = 0

def DFS(numbers, target, index, value):
    global answer
    if (index == len(numbers) and target == value):
        answer += 1
        return
    if (index == len(numbers)):
        return
    DFS(numbers, target, index + 1, value + numbers[index])
    DFS(numbers, target, index + 1, value - numbers[index])

def solution(numbers, target):
    global answer
    DFS(numbers, target, 0, 0)
    return answer

print(solution([1,2,5,6,3,1], 8))
print(solution([1,2,5,6,3,1,2,1,7], 10))
# return 26