def solution1(n):
    domain = [1, 0]
    i = 2
    while True:
        if i == n:
            return (domain[0] + domain[1]) % 1234567
        else:
            domain = [domain[0] + domain[1], domain[0]]
            i += 1

def solution2(n):
    domain = [1, 0]
    i = 2
    while i != n:
        domain = [domain[0] + domain[1], domain[0]]
        i += 1
    return (domain[0] + domain[1]) % 1234567

# solution1이 미세하게 빠른데 메모리는 약간 더 많이 쓰는데 왜죠
# 테스트 13
# solution1 120.43, 10.8MB
# solution2 122.29, 10.6MB

def solution3(n):
    domain = [1, 0]
    i = 2
    while i != n:
        domain = [sum(domain), domain[0]]
        i += 1
    return sum(domain) % 1234567
# sum(domain)과 domain[0] + domain[1]이랑 같은 연산일 거라고 생각했는데 sum()이 훨씬 시간을 많이 사용함
# 테스트 13번 기준 203.88ms, 10.8MB


def solution(n):
    domain = [1, 0]
    i = 2
    while True:
        if i == n:
            return sum(domain) % 1234567
        else:
            domain = [domain[0] + domain[1], domain[0]]
            i += 1
# ??? 그런데 1번과 3번을 조합하여 return에서만 sum()을 사용한 게 더 빠름
# 테스트 13번 기준 120.32ms, 10.8MB