# 오른쪽에서 왼쪽 방향으로 리스트 원소를 검색하여 자신보다 큰 단 하나의 값을 찾는 문제

# 2중 for(N, -1, -1)문(역순)으로 문제를 풀어야 할까?
# 1번 for:문은 왼쪽 방향으로 송신자가 신호를 보내는 부분
# 2번 for:문은 신호를 받을 수신자를 탐색하는 부분
# if:문으로 송신자의 높이(값)보다 수신자의 높이(값)가 높으면 리스트에서의 수신자의 위치(j+1)를 반환하고 2번 for:문을 빠져나감(break)
# 2번 for:문이 끝날 때까지 answer 리스트에 추가된 값이 없으면 0을 추가해 줌
# answer 리스트는 왼쪽에서 오른쪽 방향으로 작성되었으므로 reverse 해 줌

def solution(heights):
    answer = []
    for i in range(len(heights)-1, -1, -1):     # (,-1,)에서 -1이면 for()문이 끝나므로 배열의 0번째 값까지 확인하기 위해서는 -1로 설정함
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                # print("송신자 :", heights[i], ", 수신자 :", heights[j], ", 수신자 위치 :", j)
                answer += [j+1]     # 배열이 0부터 시작됨을 고려
                break
        if len(answer) < len(heights)-i:
            answer += [0]
    answer.reverse()
    return answer

print(solution([6,9,5,7,4]))
print(solution([3,9,9,3,5,7,2]))
print(solution([1,5,3,6,7,6,5]))