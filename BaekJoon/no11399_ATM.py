import sys

'''def ATM():
    N = int(sys.stdin.readline())
    P = list(map(int, sys.stdin.readline().split()))
    Li = list()

    # 인덱스를 가진 2차원.......? 이거 필요 없는 것 같은데 왜 썼지? 다시 코드 짜보겠음
    for i in range(N):
        Li += [[i, P[i]]]

    Li.sort(key = lambda x : x[1])

    for i in range(1, N):
        Li[i][1] = Li[i-1][1] + Li[i][1]

    return sum(sum(Li, [])[1::2])'''

def ATM():
    N = int(sys.stdin.readline())
    P = list(map(int, sys.stdin.readline().split()))

    P = sorted(P)

    for i in range(1, N):
        P[i] = P[i-1] + P[i]

    return sum(P)


print(ATM())