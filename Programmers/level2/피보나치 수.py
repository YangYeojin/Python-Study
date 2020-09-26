# 굳이 문제에서 주어진 순서로 생각할 필요 없는 것 같음
# 반복문을 사용하여 [a + (a-1), a]의 형식으로 풀면 될 듯

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
# 그런데 "return"에서만 sum()을 사용한 게 아예 안쓴 것보다 약간 더 빠름


def solution(n):
    domain1, domain2 = 1, 0
    i = 2
    while True:
        if i == n:
            return (domain1 + domain2) % 1234567
        else:
            domain1, domain2 = domain1 + domain2, domain1
            i += 1
# 혹시나 하고 배열을 풀고 각자 변수로 할당해 봤는데 더 빨라짐
# 테스트 13번 기준 114.07ms, 10.7MB
