import math

def solution(n, m):
    answer = []
    # 최대공약수
    answer.append(math.gcd(n,m))
    # 최소공배수
    ## //는 소수점 이하를 버리는 나누기 연산자
    answer.append(n*m//math.gcd(n,m))
    return answer