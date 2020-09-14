import sys

N, K = map(int, sys.stdin.readline().split())
cnt = 0
while N != 1:
    cnt += 1
    if N % K == 0:
        N = N / K
    else:
        N = N - 1

print(cnt)