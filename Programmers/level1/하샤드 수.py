def solution(x):
    answer = False
    if x % sum(map(int, list(str(x)))) == 0:
        answer = True
    return answer

print(solution(10))