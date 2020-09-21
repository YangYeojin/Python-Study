import sys


def knight():
    N = list(sys.stdin.readline())
    x, y = ord(N[0]) - 96, int(N[1])
    cnt = 0

    # 1번
    if x > 2:
        if y > 1:
            cnt += 1
        if y < 8-1:
            cnt += 1
    if x < 8-2:
        if y > 1:
            cnt += 1
        if y < 8-1:
            cnt += 1

    # 2번
    if y > 2:
        if x > 1:
            cnt += 1
        if x < 8-1:
            cnt += 1
    if y < 8-2:
        if x > 1:
            cnt += 1
        if x < 8-1:
            cnt += 1

    return cnt


print(knight())

# 18분