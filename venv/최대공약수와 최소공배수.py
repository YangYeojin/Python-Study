import math

def solution(n, m):
    answer = []
    #최대공약수
    answer.append(math.gcd(n,m))
    #최소공배수
    answer.append(n*m//math.gcd(n,m))
    return answer