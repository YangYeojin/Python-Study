import sys


def game():
    N, M = map(int, sys.stdin.readline().split())
    A, B, d = map(int, sys.stdin.readline().split())
    GMap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    cnt = 1

    GMap[A][B] = 2

    while True:
        if GMap[A-1][B] != 0 and GMap[A][B+1] != 0 and GMap[A+1][B] != 0 and GMap[A][B-1] != 0:
            if d == 0 and GMap[A+1][B] != 1:
                A += 1
            elif d == 1 and GMap[A][B-1] != 1:
                B -= 1
            elif d == 2 and GMap[A-1][B] != 1:
                A -= 1
            elif d == 3 and GMap[A][B+1] != 1:
                B += 1
            else:
                return cnt
        else:
            d = (d + 3) % 4     # 왼쪽 방향을 바라봄
            if d == 0 and GMap[A-1][B] == 0:
                A -= 1
                GMap[A][B] = 2
                cnt += 1
            elif d == 1 and GMap[A][B+1] == 0:
                B += 1
                GMap[A][B] = 2
                cnt += 1
            elif d == 2 and GMap[A+1][B] == 0:
                A += 1
                GMap[A][B] = 2
                cnt += 1
            elif d == 3 and GMap[A][B-1] == 0:
                B -= 1
                GMap[A][B] = 2
                cnt += 1


print(game())