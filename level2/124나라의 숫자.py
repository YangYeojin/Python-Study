'''def solution(n):
    answer = ''
    m = 3  # 제곱수
    while n != 0:
        this = n % m

        if this == 0:
            answer = '4' + answer
        elif this == 1:
            answer = '1' + answer
        else:
            answer = '2' + answer
        n = n - this ### 이 파트를 txt 파일 드래그 한 부분 고려해서 다시 작성하면?
        m *= 3  ### 이렇게 하면 안될 듯 ** 사용하는 방식으로 변경해보자
    return answer'''

### 몰라

def solution(n):
    if n <= 3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + '124'[r]

print(solution(5))
print(solution(11))
print(solution(17))