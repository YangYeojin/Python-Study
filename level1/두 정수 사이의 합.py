def solution(a, b):
    answer = 0

    if a > b:           # a가 b보다 클 때 a와 b의 값을 서로 변경해 줌
        a = a + b
        b = a - b
        a = a - b

    c = b - a + 1       # for 문을 몇 번 돌릴지 정함

    for i in range(c):  # 작은 값에 i(0부터)씩 더해서 answer 에 더해줌
        answer += (a + i)
    return answer