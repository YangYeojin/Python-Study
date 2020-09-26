import sys

def suger():
    N = int(sys.stdin.readline())
    cnt = 0
    while N > 0:
        cnt += 1
        if N % 5 == 0:
            N = N - 5
        elif N % 3 == 0:
            N = N - 3
        elif N > 5:
            N = N - 5
        elif N > 3:
            N = N - 3
        else:
            return -1
    return cnt

print(suger())