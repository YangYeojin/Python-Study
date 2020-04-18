import timeit
start = timeit.default_timer()
'''
def solution(n):
    answer = 0
    # 1. 0과 1은 소수찾기에서 계산할 필요가 없으므로 2부터 소수찾기 시작
    for i in range(2, n+1):
        # 2. for 문에서 현재 소수 찾기 검증 중인 수의 제곱근을 구한다.
        # 2부터 나온 수의 제곱근까지 중에서 나누어 떨어지는 것이 없을 때 소수임을 확인할 수 있음
        square_root_int = int(i ** 0.5)
        prime = True
        for j in range(2, square_root_int+1):
            if i % j is 0:
                prime = False
        if prime is True:
            print("i:", i)
            answer += 1
    return answer
# 100만을 2중 for:문으로 돌릴 때 메모리를 아끼려고 bool 형식을 사용했지만 시간초과
'''

'''
def solution(n):
    answer = 0
    if n >= 2: answer += 1
    if n >= 3: answer += 1
    if n >= 5: answer += 1
    # 1. 0과 1은 소수찾기에서 계산할 필요가 없으므로 2부터 소수찾기 시작
    for i in range(1, n+1, 2):
        # 2. for 문에서 현재 소수 찾기 검증 중인 수의 제곱근을 구한다.
        # 2부터 나온 수의 제곱근까지 중에서 나누어 떨어지는 것이 없을 때 소수임을 확인할 수 있음
        square_root_int = int(i ** 0.5)
        prime = True
        if i > 1 and (i%3 != 0 and i%5 != 0):
            for j in range(2, square_root_int+1):
                if i % j is 0:
                    prime = False
            if prime is True:
                print("i:", i)
                answer += 1
    return answer
#2,3,5의 배수를 제거해주었지만 시간 초과
'''


def solution(n):
    def smaller_than_100(num):
        ans = 0
        # 1. 2부터 소수찾기 시작 (문제의 제한조건, 0과 1은 소수 찾기에서 고려할 필요 없음)
        for i in range(2, n + 1):
            prime = True    # 소수 = True
            # 2. for: 현재 소수 찾기 검증 중인 수의 제곱근 확인
            square_root_int = int(i ** 0.5)
            # 3. for: i를 2부터(1로 나누었을 때 모든 값이 0이 되는 문제를 피함) 제곱근까지 나누어보며 소수 검증
            for j in range(2, square_root_int + 1):
                if i % j is 0:
                    prime = False
            # 4. i가 소수일 때 prime(소수) 변수에 1을 더함
            if prime is True:
                ans += 1
        return ans

    def bigger_than_100(num):
        ans = 25
        prime_smaller_than_100 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        # 101부터 소수 찾기 시작 (2의 배수는 무시함)
        for i in range(101, n + 1, 2):
            prime_s100 = 0
            prime = True
            square_root_int = int(i ** 0.5)
            # i가 100 이하의 소수로 나누어 떨어지는지 확인
            for j in range(len(prime_smaller_than_100)):
                if i % prime_smaller_than_100[j] == 0:
                    prime_s100 += 1
            # i가 100 이하의 모든 소수들로 나누어 떨어지지 않으면 소수를 구함
            if prime_s100 == 0:
                for j in range(101, square_root_int + 1, 2):
                    if i % j is 0:
                        prime = False
                if prime is True:
                    ans += 1
        return ans

    if n <= 100:
        answer = smaller_than_100(n)
    else:
        answer = bigger_than_100(n)
    return answer

print(solution(1000000))
stop = timeit.default_timer()
print(stop - start)
# 답 : 78498
# 실행시간 : 5.4507475