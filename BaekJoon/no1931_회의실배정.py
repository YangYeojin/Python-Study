import sys

def meetingRoom():
    N = int(sys.stdin.readline())
    Is = list()

    for i in range(N):
        Is += [list(map(int, sys.stdin.readline().split()))]

    Is = sorted(Is)
    Is = sorted(Is, key = lambda x: x[1])

    cnt = 1
    meetingEnd = Is[0][1]
    for i in range(1, N):
        if Is[i][0] >= meetingEnd:
            cnt += 1
            meetingEnd = Is[i][1]
    return cnt


print(meetingRoom())