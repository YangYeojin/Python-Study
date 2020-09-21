import sys


def direction():
    N = int(sys.stdin.readline())
    cnt = 0

    for h in range(N+1):
        if h // 10 == 3 or h % 10 == 3:
            cnt += 3600
            continue
        for m in range(60):
            if m // 10 == 3 or m % 10 == 3:
                cnt += 60
                continue
            for s in range(60):
                if s // 10 == 3 or s % 10 == 3:
                    cnt += 1
    print(cnt)


direction()

# 9분